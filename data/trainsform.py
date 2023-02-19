# Adapted from: IEEE VIP Cup 2022 - https://www.grip.unina.it/download/vipcup2022/random_operations.py

import os
from PIL import Image
from tqdm import tqdm
import shutil
import glob
from random import Random
from joblib import Parallel, delayed
import pandas as pd
import warnings

# Configuirations
OUTPUT_SIZE  = 200
CROPSIZE_MIN = 160
CROPSIZE_MAX = 2048
CROPSIZE_RATIO = (5,8)
QF_RANGE = (65, 100)

def check_img(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff', '.bmp', '.gif'))
            
def transform(input_dir, output_dir, seed, maximg=None):
    """
    Transforms images in the input directory by performing random operations such as cropping, resizing, and jpeg compression.

    Args:
    input_dir (str): The directory path containing the source images to be transformed. It can include wildcards (*) to match multiple directories.
    output_dir (str): The directory path to save the transformed images.
    seed (int): The seed to use for random operations.
    maximg (int, optional): The maximum number of images to be transformed. If None, all images in the input directory will be transformed. Default is None.

    Returns:
    None
    """
    print('Random Operations from ', input_dir, 'to', output_dir, flush=True)
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)  # remove existing output directory
    os.makedirs(output_dir)  # create output directory
    
    random = Random(seed) # set seed 
    
    # list fo images
    input_dir = input_dir if '*' in input_dir else os.path.join(input_dir, '**/*')
    list_src = [_ for _ in sorted(glob.glob(input_dir,  recursive=True)) if check_img(_)]
    
    if maximg is not None:
        random.shuffle(list_src)  # shuffle the list of images
        list_src = list_src[:maximg]  # limit the number of images
        
    def transform(index, src):
        filename_dst = 'img%06d.jpg' % index
        if (len(src.split("/"))<=4 and "/kaggle" not in src) or (len(src.split("/"))<=5 and "/kaggle" in src):
            sub_dir = ''
        else :
            sub_dir = src.split("/",4)[-1] if '/kaggle' in src else src.split("/",3)[-1]
            sub_dir = sub_dir.rsplit('/',1)[0] # remove name
        os.makedirs(os.path.join(output_dir, sub_dir), exist_ok=True)
        dst = os.path.join(output_dir, sub_dir, filename_dst)

        # open image
        with Image.open(src) as img:
            img = img.convert('RGB')
            height = img.size[1]
            width = img.size[0]

            # select the size of crop
            cropmax = min(min(width, height), CROPSIZE_MAX)
            if cropmax<CROPSIZE_MIN:
                warnings.warn("{} - ({},{}) is too small".format(src, height, width))
                return [None]*7
            
            cropmin = max(cropmax*CROPSIZE_RATIO[0]//CROPSIZE_RATIO[1], CROPSIZE_MIN)
            cropsize = random.randint(cropmin, cropmax)

            # select the type of interpolation
            interp = Image.ANTIALIAS if cropsize>OUTPUT_SIZE else Image.CUBIC

            # select the position of the crop
            x1 = random.randint(0, width - cropsize)
            y1 = random.randint(0, height - cropsize)

            # select the jpeg quality factor
            qf = random.randint(*QF_RANGE)

            # make cropping
            img = img.crop((x1, y1, x1+cropsize, y1+cropsize))
            assert img.size[0]==cropsize
            assert img.size[1]==cropsize

            # make resizing
            img = img.resize((OUTPUT_SIZE, OUTPUT_SIZE), interp)
            assert img.size[0]==OUTPUT_SIZE
            assert img.size[1]==OUTPUT_SIZE

            # make jpeg compression
            img.save(dst, "JPEG", quality = qf)
        
        return [filename_dst,dst,src,cropsize,x1,y1,qf]
    
    metainfo = Parallel(n_jobs=-1, backend='threading')(
        delayed(transform)(index, src) for index, src in enumerate(tqdm(list_src))
        )
    metainfo = pd.DataFrame(metainfo, columns=['filename','dst','src','cropsize','x1','y1','qf'])
    output_csv = os.path.join(output_dir, "metadata.csv")
    metainfo.to_csv(output_csv, index=False)
            
if __name__=='__main__':
    from sys import argv
    input_dir   = argv[1]
    output_dir  = argv[2]
    seed        = int(argv[3])
    maximg      = int(argv[4]) if len(argv)>4 else None
    transform(input_dir, output_dir, seed, maximg)
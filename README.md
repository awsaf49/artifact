# ArtiFact: A Large-Scale Dataset with Artificial and Factual Images for Generalizable and Robust Synthetic Image Detection [ICIP 2023]

<img src="images/header.png">

**Paper:** 
* IEEE Xplore: https://ieeexplore.ieee.org/document/10222083
* ArXiv: https://arxiv.org/abs/2302.11970

**Abstract:** Synthetic image generation has opened up new  opportunities but has also created threats in regard to privacy, authenticity, and security. Detecting fake images is of paramount importance to prevent illegal activities, and previous research has shown that generative models leave unique patterns in their synthetic images that can be exploited to detect them. However, the fundamental problem of generalization remains, as even state-of-the-art detectors encounter difficulty when facing generators never seen during training. To assess the generalizability and robustness of synthetic image detectors in the face of real-world impairments, this paper presents a large-scale dataset named ArtiFact, comprising diverse generators, object categories, and real-world challenges. Moreover, the proposed multi-class classification scheme, combined with a filter stride reduction strategy addresses social platform impairments and effectively detects synthetic images from both seen and unseen generators. The proposed solution significantly outperforms other top teams by 8.34% on Test 1, 1.26% on Test 2, and 15.08% on Test 3 in the IEEE VIP Cup challenge at ICIP 2022, as measured by the accuracy metric.

**Presentation**:
[![YouTube](https://badges.aleen42.com/src/youtube.svg)](https://youtu.be/hGXufeubNME)

**Visual Summary**:

<div align="center"> <img src="images\visual_summary2.jpg" width="700"> </div>

# Update
* [22 June 2023] - The work has been accepted to IEEE ICIP 2023 conference.

# Result on [IEEE VIP Cup at ICIP 2022](https://grip-unina.github.io/vipcup2022/)

Accuracy (%) of Top3 Teams on Leaderboard,

| Team Names            | Test 1     | Test 2     | Test 3     |
| :-------------------- | :--------: | :--------: | :--------: |
| Sherlock              | 87\.70     | 77\.52     | 73\.45     |
| FAU Erlangen-Nürnberg | 87\.14     | 81\.74     | 75\.52     |
| **Megatron (Ours)**   | **96\.04** | **83\.00** | **90\.60** |

> **Note:** A small portion of the proposed ArtiFact dataset, totaling 222K images of 71K real images and 151K fake images from only 13 generators is used in the IEEE VIP Cup. Here all the Test data is kept confidential from all participating teams. Additionally, the generators used for the Test 1 data are known to all teams, whereas the generators for Test 2 and Test 3 are kept undisclosed.

# Dataset Description
* Total number of images: $2,496,738$
* Number of real images: $964,989$
* Number of fake images: $1,531,749$
* Number of generators used for fake images: $25$ (including $13$ GANs, $7$ Diffusion, and $5$ miscellaneous generators)
* Number of sources used for real images: $8$
* Categories included in the dataset: `Human/Human Faces`, `Animal/Animal Faces`, `Places`, `Vehicles`, `Art`, and other real-life objects
* Image Resolution: $200 \times 200$

## Data Distribution

* Real 

<div align="center"> <img src="images\artifact-real-v4.png" width="700"> </div>

* Fake

<div align="center"> <img src="images\artifact-fake-v4.png" width="800"> </div>

# Download Dataset

The dataset is hosted on Kaggle. The dataset can be downloaded i) directly from the browser using the link below or ii) can be downloaded using [kaggle-api](https://github.com/Kaggle/kaggle-api).

## i) Directly from Browser
Link: [ArtiFact Dataset](https://www.kaggle.com/datasets/awsaf49/artifact-dataset)


## ii) Kaggle API
```shell
!kaggle datasets download -d awsaf49/artifact-dataset
```

# How to Use
The dataset is organized into folders, each of which corresponds to a specific generator of synthetic images or source of real images. Each folder contains a `metadata.csv` file, which provides information about the images in the folder. It contains following columns,

* `image_path` : The relative path of the image file.
* `target` : The label for the image, which is either 0 for real or 1 for fake.
* `category` : The category (cat or dog etc) of the image


# Data Generation

* Images are randomly sampled from different methods then transformed using impairments. The methods are listed below,
    <details close>
    <summary>Methods</summary>
    

    |                 |                                                |                                            |                                     |                                               |                                                |                                                    |                                                                   |                                                   |                                                 |                                             |                                             |                                                              |                                                       |                                            |                                           |                                                  |                                                   |                                                                             |                                            |                                                                                           |                                           |                                           |                                                                               |                                               |                                                              |                                                     |                                                     |                                                           |                                                   |                                                        |                                         |                                                                   |                                                                 |
    | :-------------- | :--------------------------------------------- | :----------------------------------------- | :---------------------------------- | :-------------------------------------------- | :--------------------------------------------- | :------------------------------------------------- | :---------------------------------------------------------------- | :------------------------------------------------ | :---------------------------------------------- | :------------------------------------------ | :------------------------------------------ | :----------------------------------------------------------- | :---------------------------------------------------- | :----------------------------------------- | :---------------------------------------- | :----------------------------------------------- | :------------------------------------------------ | :-------------------------------------------------------------------------- | :----------------------------------------- | :---------------------------------------------------------------------------------------- | :---------------------------------------- | :---------------------------------------- | :---------------------------------------------------------------------------- | :-------------------------------------------- | :----------------------------------------------------------- | :-------------------------------------------------- | :-------------------------------------------------- | :-------------------------------------------------------- | :------------------------------------------------ | :----------------------------------------------------- | :-------------------------------------- | :---------------------------------------------------------------- | :-------------------------------------------------------------- |
    | **Method** | ImageNet                                       | COCO                                       | LSUN                                | AFHQ                                          | FFHQ                                           | Metfaces                                           | CelebAHQ                                                          | Landscape                                         | Glide                                           | StyleGAN2                                   | StyleGAN3                                   | Generative Inpainting                                        | Taming Transformer                                    | MAT                                        | LaMa                                      | Stable Diffusion                                 | VQ Diffusion                                      | Palette                                                                     | StyleGAN1                                  | Latent Diffusion                                                                          | CIPS                                      | StarGAN                                   | BigGAN                                                                        | GANformer                                     | ProjectedGAN                                                 | SFHQ                                                | FaceSynthetics                                      | Denoising Diffusion GAN                                   | DDPM                                              | DiffusionGAN                                           | GauGAN                                  | ProGAN                                                            | CycleGAN                                                        |
    | **Reference** | [link](https://www.image-net.org/download.php) | [link](https://cocodataset.org/\#download) | [link](https://github.com/fyu/lsun) | [link](https://github.com/clovaai/stargan-v2) | [link](https://github.com/NVlabs/ffhq-dataset) | [link](https://github.com/NVlabs/metfaces-dataset) |  [link](https://github.com/tkarras/progressive*growing*of*gans) | [link](https://github.com/mahmoudnafifi/HistoGAN) | [link](https://github.com/openai/glide-text2im) | [link](https://github.com/NVlabs/stylegan2) | [link](https://github.com/NVlabs/stylegan3) |  [link](https://github.com/JiahuiYu/generative*inpainting) | [link](https://github.com/CompVis/taming-transformer) | [link](https://github.com/fenglinglwb/mat) | [link](https://github.com/saic-mdal/lama) | [link](https://github.com/huggingface/diffusers) | [link](https://github.com/microsoft/VQ-Diffusion) | [link](https://github.com/Janspiry/Palette-Image-to-Image-Diffusion-Models) | [link](https://github.com/NVlabs/stylegan) | [link](https://github.com/compvis/latent-diffusion\#retrieval-augmented-diffusion-models) | [link](https://github.com/saic-mdal/CIPS) | [link](https://github.com/yunjey/StarGAN) | [link](https://github.com/open-mmlab/mmgeneration/tree/master/configs/biggan) | [link](https://github.com/dorarad/gansformer) |  [link](https://github.com/autonomousvision/projected*gan) | [link](https://github.com/SelfishGene/SFHQ-dataset) | [link](https://github.com/microsoft/FaceSynthetics) | [link](https://github.com/NVlabs/denoising-diffusion-gan) | [link](https://github.com/hojonathanho/diffusion) | [link](https://github.com/Zhendong-Wang/Diffusion-GAN) | [link](https://github.com/NVlabs/SPADE) |  [link](https://github.com/tkarras/progressive*growing*of*gans) | [link](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) |
    
    </details>

* All images went through RandomCrop and Random Impairments (Jpeg Compression & Downscale). To apply these transformation use [data/transform.py](https://github.com/awsaf49/artifact/blob/main/data/transform.py) which applies random transformation. All images are cropped and resized to $200 \times 200$ pixels and then compressed using JPEG at a random quality level.

```shell
!python data/transform.py <input directory> <output directory> <seed>
```

# Citation
```bibtex
@INPROCEEDINGS{artifact,
  author={Rahman, Md Awsafur and Paul, Bishmoy and Sarker, Najibul Haque and Hakim, Zaber Ibn Abdul and Fattah, Shaikh Anowarul},
  booktitle={2023 IEEE International Conference on Image Processing (ICIP)}, 
  title={Artifact: A Large-Scale Dataset With Artificial And Factual Images For Generalizable And Robust Synthetic Image Detection}, 
  year={2023},
  volume={},
  number={},
  pages={2200-2204},
  doi={10.1109/ICIP49359.2023.10222083}}
```

# License

ArtiFact dataset takes leverage of data from multiple methods thus different parts of the dataset come with different licenses. All the methods and their associated licenses are mentioned in the table,

<details close>
<summary>Data License</summary>


| Method                  | License                                                                                |
|:------------------------|:---------------------------------------------------------------------------------------|
| ImageNet                | Non Commercial                                                                         |
| COCO                    | Creative Commons Attribution 4.0 License                                               |
| LSUN                    | Unknown                                                                                |
| AFHQ                    | Creative Commons Attribution-NonCommercial 4.0 International Public                    |
| FFHQ                    | Creative Commons BY-NC-SA 4.0 license                                                  |
| Metfaces                | Creative Commons BY-NC 2.0                                                             |
| CelebAHQ                | Creative Commons Attribution-NonCommercial 4.0 International Public                    |
| Landscape               | MIT license                                                                            |
| Glide                   | MIT license                                                                            |
| StyleGAN2               | Nvidia Source Code License                                                             |
| StyleGAN3               | Nvidia Source Code License                                                             |
| Generative Inpainting   | Creative Commons Public Licenses                                                       |
| Taming Transformer      | MIT License                                                                            |
| MAT                     | Creative Commons Public Licenses                                                       |
| LaMa                    | Apache-2.0 License                                                                     |
| Stable Diffusion        | Apache-2.0 License                                                                     |
| VQ Diffusion            | MIT License                                                                            |
| Palette                 | MIT License                                                                            |
| StyleGAN1               | Creative Commons Public Licenses                                                       |
| Latent Diffusion        | MIT License                                                                            |
| CIPS                    | MIT License                                                                            |
| StarGAN                 | MIT License                                                                            |
| BigGAN                  | MIT License                                                                            |
| GANformer               | MIT License                                                                            |
| ProjectedGAN            | MIT License                                                                            |
| SFHQ                    | MIT License                                                                            |
| FaceSynthetics          | Research Use of Data Agreement v1.0                                                    |
| Denoising Diffusion GAN | NVIDIA License                                                                         |
| DDPM                    | Unknown                                                                                |
| DiffusionGAN            | MIT License                                                                            |
| GauGAN                  | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License |
| ProGAN                  | Attribution-NonCommercial 4.0 International                                            |
| CycleGAN                | BSD                                                                                    |


</details>

# Acknowledgment

* The authors would like to express their gratitude to the IEEE Signal Processing Society, GRIP of the University Federico II of Naples (Italy), and NVIDIA (USA) for hosting the [IEEE Video and Image Processing (VIP) Cup](https://grip-unina.github.io/vipcup2022/) competition at ICIP 2022. This competition provided a platform for the authors to showcase their work and motivated them to push their boundaries to deliver a state-of-the-art solution.

* The authors also would like to express their gratitude to the authors of the methods that is used for creating ArtiFact dataset. All the methods and their reference is added below,
    <details close>
    <summary>Data Reference</summary>

    | Method                  | Reference                                                                                |
    |:------------------------|:-----------------------------------------------------------------------------------------|
    | ImageNet                | [link](https://www.image-net.org/download.php)                                           |
    | COCO                    | [link](https://cocodataset.org/#download)                                                |
    | LSUN                    | [link](https://github.com/fyu/lsun)                                                      |
    | AFHQ                    | [link](https://github.com/clovaai/stargan-v2)                                            |
    | FFHQ                    | [link](https://github.com/NVlabs/ffhq-dataset)                                           |
    | Metfaces                | [link](https://github.com/NVlabs/metfaces-dataset)                                       |
    | CelebAHQ                | [link](https://github.com/tkarras/progressive_growing_of_gans)                           |
    | Landscape               | [link](https://github.com/mahmoudnafifi/HistoGAN)                                        |
    | Glide                   | [link](https://github.com/openai/glide-text2im)                                          |
    | StyleGAN2               | [link](https://github.com/NVlabs/stylegan2)                                              |
    | StyleGAN3               | [link](https://github.com/NVlabs/stylegan3)                                              |
    | Generative Inpainting   | [link](https://github.com/JiahuiYu/generative_inpainting)                                |
    | Taming Transformer      | [link](https://github.com/CompVis/taming-transformer)                                    |
    | MAT                     | [link](https://github.com/fenglinglwb/mat)                                               |
    | LaMa                    | [link](https://github.com/saic-mdal/lama)                                                |
    | Stable Diffusion        | [link](https://github.com/huggingface/diffusers)                                         |
    | VQ Diffusion            | [link](https://github.com/microsoft/VQ-Diffusion)                                        |
    | Palette                 | [link](https://github.com/Janspiry/Palette-Image-to-Image-Diffusion-Models)              |
    | StyleGAN1               | [link](https://github.com/NVlabs/stylegan)                                               |
    | Latent Diffusion        | [link](https://github.com/compvis/latent-diffusion#retrieval-augmented-diffusion-models) |
    | CIPS                    | [link](https://github.com/saic-mdal/CIPS)                                                |
    | StarGAN                 | [link](https://github.com/yunjey/StarGAN)                                                |
    | BigGAN                  | [link](https://github.com/open-mmlab/mmgeneration/tree/master/configs/biggan)            |
    | GANformer               | [link](https://github.com/dorarad/gansformer)                                            |
    | ProjectedGAN            | [link](https://github.com/autonomousvision/projected_gan)                                |
    | SFHQ                    | [link](https://github.com/SelfishGene/SFHQ-dataset)                                      |
    | FaceSynthetics          | [link](https://github.com/microsoft/FaceSynthetics)                                      |
    | Denoising Diffusion GAN | [link](https://github.com/NVlabs/denoising-diffusion-gan)                                |
    | DDPM                    | [link](https://github.com/hojonathanho/diffusion)                                        |
    | DiffusionGAN            | [link](https://github.com/Zhendong-Wang/Diffusion-GAN)                                   |
    | GauGAN                  | [link](https://github.com/NVlabs/SPADE)                                                  |
    | ProGAN                  | [link](https://github.com/tkarras/progressive_growing_of_gans)                           |
    | CycleGAN                | [link](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)                          |

    </details>

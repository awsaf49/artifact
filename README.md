# Robust Synthetic Image Detection with Multi-class Scheme and Filter Stride Reduction

Paper:

Abstract:

## Result on IEEE VIP Cup at ICIP 2022

Accuracy (%) of Top3 Teams on Leaderboard,
| Team Names            | Test 1     | Test 2     | Test 3     |
| :-------------------- | :--------: | :--------: | :--------: |
| Sherlock              | 87\.70     | 77\.52     | 73\.45     |
| FAU Erlangen-Nürnberg | 87\.14     | 81\.74     | 75\.52     |
| **Megatron (Ours)**   | **96\.04** | **83\.00** | **90\.60** |

> **Note:** The Test data is kept confidential from all participating teams. Additionally, the generators used for the Test 1 data are known to all teams, whereas the generators for Test 2 and Test 3 are kept undisclosed.

# ArtiFact: Artificial and Factual Dataset

<img src="images/header.png">

## Download Dataset

The dataset is hosted on Kaggle. The dataset can be downloaded directly from the browser using link below or can be downloaded using [kaggle-api](https://github.com/Kaggle/kaggle-api) using following method.

Link: [ArtiFact]()

## Data Generation

* Images are randomly sampled from different methods then transformed using impairments. The methods are listed below,
    <details close>
    <summary>Methods</summary>

    |                 |                                                |                                            |                                     |                                               |                                                |                                                    |                                                                   |                                                   |                                                 |                                             |                                             |                                                              |                                                       |                                            |                                           |                                                  |                                                   |                                                                             |                                            |                                                                                           |                                           |                                           |                                                                               |                                               |                                                              |                                                     |                                                     |                                                           |                                                   |                                                        |                                         |                                                                   |                                                                 |
    | :-------------- | :--------------------------------------------- | :----------------------------------------- | :---------------------------------- | :-------------------------------------------- | :--------------------------------------------- | :------------------------------------------------- | :---------------------------------------------------------------- | :------------------------------------------------ | :---------------------------------------------- | :------------------------------------------ | :------------------------------------------ | :----------------------------------------------------------- | :---------------------------------------------------- | :----------------------------------------- | :---------------------------------------- | :----------------------------------------------- | :------------------------------------------------ | :-------------------------------------------------------------------------- | :----------------------------------------- | :---------------------------------------------------------------------------------------- | :---------------------------------------- | :---------------------------------------- | :---------------------------------------------------------------------------- | :-------------------------------------------- | :----------------------------------------------------------- | :-------------------------------------------------- | :-------------------------------------------------- | :-------------------------------------------------------- | :------------------------------------------------ | :----------------------------------------------------- | :-------------------------------------- | :---------------------------------------------------------------- | :-------------------------------------------------------------- |
    | **Method** | ImageNet                                       | COCO                                       | LSUN                                | AFHQ                                          | FFHQ                                           | Metfaces                                           | CelebAHQ                                                          | Landscape                                         | Glide                                           | StyleGAN2                                   | StyleGAN3                                   | Generative Inpainting                                        | Taming Transformer                                    | MAT                                        | LaMA                                      | Stable Diffusion                                 | VQ Diffusion                                      | Palette                                                                     | StyleGAN1                                  | Latent Diffusion                                                                          | CIPS                                      | StarGAN                                   | BigGAN                                                                        | GANformer                                     | ProjectedGAN                                                 | SFHQ                                                | FaceSynthetics                                      | Denoising Diffusion GAN                                   | DDPM                                              | DiffusionGAN                                           | GauGAN                                  | ProGAN                                                            | CycleGAN                                                        |
    | **Reference** | [link](https://www.image-net.org/download.php) | [link](https://cocodataset.org/\#download) | [link](https://github.com/fyu/lsun) | [link](https://github.com/clovaai/stargan-v2) | [link](https://github.com/NVlabs/ffhq-dataset) | [link](https://github.com/NVlabs/metfaces-dataset) |  [link](https://github.com/tkarras/progressive*growing*of*gans) | [link](https://github.com/mahmoudnafifi/HistoGAN) | [link](https://github.com/openai/glide-text2im) | [link](https://github.com/NVlabs/stylegan2) | [link](https://github.com/NVlabs/stylegan3) |  [link](https://github.com/JiahuiYu/generative*inpainting) | [link](https://github.com/CompVis/taming-transformer) | [link](https://github.com/fenglinglwb/mat) | [link](https://github.com/saic-mdal/lama) | [link](https://github.com/huggingface/diffusers) | [link](https://github.com/microsoft/VQ-Diffusion) | [link](https://github.com/Janspiry/Palette-Image-to-Image-Diffusion-Models) | [link](https://github.com/NVlabs/stylegan) | [link](https://github.com/compvis/latent-diffusion\#retrieval-augmented-diffusion-models) | [link](https://github.com/saic-mdal/CIPS) | [link](https://github.com/yunjey/StarGAN) | [link](https://github.com/open-mmlab/mmgeneration/tree/master/configs/biggan) | [link](https://github.com/dorarad/gansformer) |  [link](https://github.com/autonomousvision/projected*gan) | [link](https://github.com/SelfishGene/SFHQ-dataset) | [link](https://github.com/microsoft/FaceSynthetics) | [link](https://github.com/NVlabs/denoising-diffusion-gan) | [link](https://github.com/hojonathanho/diffusion) | [link](https://github.com/Zhendong-Wang/Diffusion-GAN) | [link](https://github.com/NVlabs/SPADE) |  [link](https://github.com/tkarras/progressive*growing*of*gans) | [link](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) |
    </details>

* All images went through RandomCrop and Random Impairments (Jpeg Compression & Downscale). To apply these transformation use [data/transform.py](data/transform.py) which applies random transformation. All images are cropped and resized to $200 \times 200$ pixels and then compressed using JPEG at a random quality level.

    ```shell
    python data/transform.py <input directory> <output directory> <seed>
    ```

# Citation


# License

ArtiFact dataset take leverage of data from multiple methods thus different parts of the dataset come with different licenses. All the methods and their associated licenses are mentioned in the table,

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
| LaMA                    | Apache-2.0 License                                                                     |
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
    | LaMA                    | [link](https://github.com/saic-mdal/lama)                                                |
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

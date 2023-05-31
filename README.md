# cs230_diffusion
## Denoising Diffusion MRI & Constructing Diffusion MRI Metrics with Less Data

Diffusion-weighted Imaging (DWI) is an MRI technique that maps the diffusion process of molecules to 
microstructure in biological tissue, which is limited by image resolution and the data size. Here, 
we utilized a deep learning model to infer fractional anisotropy maps from few diffusion weighted images. 

In this project, we implemented a U-Net convolutional neural network in order to create a high quality, reduced noise, Fractional Anisotropy map (FA) from fewer diffusion directions. The inputs to this model are 6 optimized Diffusion-Weighted MRI images and one non-diffusion weighted MRI image. The output to this model is then a high-quality FA Map, which could be indicative of the underlying tissue health.

## Repository Description
This repository contains the models that were trained,notebooks used to generate data for training, 
and notebooks for testing the data. 

This project was the final course project for CS230: Deep Learning, at Stanford University, Fall 2021. The project
was an "Outstanding Project" for the course during the quarter: http://cs230.stanford.edu/past-projects/

Final Project Report can be found here: 
http://cs230.stanford.edu/projects_fall_2021/reports/103153908.pdf

The Data used for this project came from this publically available, high resolution, Brain Diffusion dataset: Fuyixue Wang, Zijing Dong, Qiyuan Tian, Congyu Liao, Qiuyun Fan, W. Scott Hoge, Boris Keil, Jonathan R. Polimeni, Lawrence L. Wald, Susie Y. Huang, and Kawin Setsompop. In vivo human whole-brain Connectom diffusion MRI dataset at 760μm isotropic resolution. Scientific Data 2021 8:1, 8(1):1–12, 4 2021.

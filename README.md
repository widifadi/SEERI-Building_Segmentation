# SEERI Building Segmentation

The provided Google Colab code is the result from the project SEERI, a collaboration between Braga Tech. and GIZ. The code will produce a vectorize building shape from deep learning process for building segmentation that will be fed to the SEERI website, which then be used for estimating solar potential on the rooftop. 

## How to Run

To run the code several data have to be downloaded first. After setting-up the folder structures in google drive which will be done automatically using the provided code, label class, image, and shapefile data has to be uploaded to the following directories:
1. label class directory: /content/drive/MyDrive/proj_name/
2. image directory: /content/drive/MyDrive/proj_name/original_data/img/
3. shapefile directory: /content/drive/MyDrive/original_data/shp/building_shp/

Label class file can be downloaded from this repository or from this [link](https://drive.google.com/file/d/1UpdSPBQbY9ZdyrcQzbrwFNcjvFXcBW8x/view?usp=sharing), and the sample data that was used in the project can be downloaded [here](https://drive.google.com/drive/folders/1lxkiN0ZqubMTWKUh7H6sy_wzHIaxgPmT?usp=sharing).

Moreover, the prediction model resulted from the training will be stored in this directory: <br /> /content/drive/MyDrive/proj_name/model/bss_model/ <br />

The prediction model that was used in the project can be downloaded [here](https://drive.google.com/drive/folders/1dweq_9_x8r_Hb6iXJpC3YqypLZjMdZP4?usp=sharing), which can then be uploaded to the directory mentioned above. 

Here are the result of model training and image segmentation process. 
![Prediction Result](https://github.com/widifadi/SEERI-Building_Segmentation/assets/82517622/650b430b-7454-4078-a5af-6a5edf923a04)
![Best IoU Plot](https://github.com/widifadi/SEERI-Building_Segmentation/assets/82517622/34f2b996-3a0a-49ae-b616-43d4b5e1d87f)
![Best Dice Loss Plot](https://github.com/widifadi/SEERI-Building_Segmentation/assets/82517622/4bfa6feb-d445-4893-83d4-1ccefe3d81d9)


### About Building Regularization

The regularization on the predicted building shape was done using the repo from: https://github.com/zorzi-s/projectRegularization, the pretrained weights needed to run the code can be downloaded from the provided [repo](https://drive.google.com/drive/folders/1IPrDpvFq9ODW7UtPAJR_T-gGzxDat_uu). The pretrained weights should be uploaded to the following directories: <br /> /content/drive/MyDrive/proj_name/model/pretrained_weights_gan/ <br />

Note that as some error occured when using regularize.py from the provided repo on google colab, the code was slightly adjusted and the modified code can be downloaded [here](https://drive.google.com/drive/folders/1LVSCoZ6nrpqBzJOb941p85l_ySJrPY4K?usp=sharing) or from this repository. 

The figure below shows the result of the building shape after regularization process.
![Regularized Result](https://github.com/widifadi/SEERI-Building_Segmentation/assets/82517622/a0effe42-dfe7-4aa6-80e7-2556b2c9670a)


## Credit 

Some of the original code that was used in the project are the following: 
* https://www.kaggle.com/code/balraj98/unet-for-building-segmentation-pytorch
* https://github.com/Hejarshahabi/GeoPatch/tree/main
* https://github.com/zorzi-s/projectRegularization
* https://github.com/s1m0nS/mapAI-regularization.git

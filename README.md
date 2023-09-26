# SEERI Building Segmentation

The provided Google Colab code is the result from the project SEERI, a collaboration between Braga Tech. and GIZ. The code will produce a vectorize building shape from deep learning process for building segmentation that will be fed to the SEERI website, which then be used for estimating solar potential on the rooftop. 

# How to Run

To run the code several data have to be downloaded first. After setting-up the folder structures in google drive which will be done automatically using the provided code, label class, image, and shapefile data has to be uploaded to the following directories:
label class directory: /content/drive/MyDrive/proj_name/
image directory: /content/drive/MyDrive/proj_name/original_data/img/
shapefile directory: /content/drive/MyDrive/original_data/shp/building_shp/

Label class file can be downloaded from this repository or from this [link](https://drive.google.com/file/d/1UpdSPBQbY9ZdyrcQzbrwFNcjvFXcBW8x/view?usp=sharing), and the sample data that was used in the project can be downloaded [here](https://drive.google.com/drive/folders/1lxkiN0ZqubMTWKUh7H6sy_wzHIaxgPmT?usp=sharing).

Moreover, the prediction model resulted from the training will be stored in this directory: /content/drive/MyDrive/proj_name/model/bss_model/
The prediction model that was used in the project can be downloaded [here](https://drive.google.com/drive/folders/1dweq_9_x8r_Hb6iXJpC3YqypLZjMdZP4?usp=sharing), which can then be uploaded to the directory mentioned above. 

# About Building Regularization

The regularization on the predicted building shape was done using the repo from: https://github.com/zorzi-s/projectRegularization, the pretrained weights needed to run the code can be downloaded from the provided [repo](https://drive.google.com/drive/folders/1IPrDpvFq9ODW7UtPAJR_T-gGzxDat_uu). The pretrained weights should be uploaded to the following directories: /content/drive/MyDrive/proj_name/model/pretrained_weights_gan/

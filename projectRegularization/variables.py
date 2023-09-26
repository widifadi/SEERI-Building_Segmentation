# CONFIGURE THE PATHS HERE: 

# TRAINING 
DATASET_RGB = "/content/drive/MyDrive/GIZ_/img_dataset/tiff/_prep/512_Manual/patch/*.tif"
DATASET_GTI = "/content/drive/MyDrive/GIZ_/img_dataset/tiff/_prep/512_Manual/label/*.tif"
DATASET_SEG = "/content/drive/MyDrive/GIZ_/img_dataset/product/prediction/Bali_R2C2/*.tif"

DEBUG_DIR = "./debug/"

# INFERENCE 
INF_RGB = "/content/drive/MyDrive/GIZ_/img_dataset/tiff/_prep/pred_data/Bali_R2C2/Prediction_patch/*.tif"
INF_SEG = "/content/drive/MyDrive/GIZ_/img_dataset/product/prediction/Bali_R2C2/*.tif"
INF_OUT = "/content/drive/MyDrive/GIZ_/img_dataset/product/regularized_imgs/Bali_R2C2/"

MODEL_ENCODER = "/content/drive/MyDrive/GIZ_/img_dataset/model/pretrained_weights_gan/E140000_e1"
MODEL_GENERATOR = "/content/drive/MyDrive/GIZ_/img_dataset/model/pretrained_weights_gan/E140000_net"

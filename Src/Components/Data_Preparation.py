# import os
# import sys

from Logger import logger 
from Utils import remove_files,load_pickle
from Constant import IMAGE_TO_TEXT_MODEL_PATH
from Entities.entity import DataPreparationConfig

from pathlib import Path
from glob import glob
from tqdm import tqdm
from bs4 import BeautifulSoup
# from transformers import pipeline

import numpy as np
import pandas as pd
import os
import cv2

corrupt_roi = []

# image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
image_to_text = load_pickle(IMAGE_TO_TEXT_MODEL_PATH)
logger.info("Image-to-text model loaded")

class DataPreparation:

    def __init__(self,config:DataPreparationConfig):

        self.TRAIN_META_DATA_FILE_PATH = config.TRAIN_META_DATA_FILE_PATH
        self.VALIDATION_META_DATA_FILE_PATH = config.VALIDATION_META_DATA_FILE_PATH

    def scale_bbox(self,original_image_shape,bb_annotations,scaled_image_shape = (224,224,3)):

        ''''
        Scaling of bounding box according to the scale of scaled images (224,224,3)
        
        '''

        height,width = original_image_shape[:2]
        scaled_height,scaled_width = scaled_image_shape[:2]


        height_factor = scaled_height/height
        width_factor = scaled_width/width


        '''
        (xmin,ymax) ---------- (xmax,ymax)
            |                     |
            |                     |
        (xmin,ymin) ---------- (xmax,ymin)

        '''


        xmin, ymin, xmax, ymax = bb_annotations

        scaled_xmin = int(np.round(xmin * width_factor))
        scaled_ymin = int(np.round(ymin * height_factor))
        scaled_xmax = int(np.round(xmax * width_factor))
        scaled_ymax = int(np.round(ymax * height_factor))

        return (scaled_xmin,scaled_ymin,scaled_xmax,scaled_ymax)



    def get_captions(self,set_type = 'train'):


        '''
        
        Creates the captions.csv file for storing captions of ROIs
        
        '''
        captions_directory_path = Path(f"Artifacts/{set_type}/captions")
        roi_directory_path = Path(f"Artifacts/{set_type}/roi")

        os.makedirs(captions_directory_path,exist_ok = True)
        remove_files(captions_directory_path.as_posix())

        captions = []
        filenames = []

        roi_img_path = os.path.join(roi_directory_path,'*')

        roi_imgs = glob(roi_img_path)

        for roi in tqdm(roi_imgs):

            filename = roi.split('/')[-1].split('.')[0]

            filenames.append(filename+'.png')
            caption = image_to_text(roi)
            captions.append(caption[0]['generated_text'])

        captions_df = pd.DataFrame({'Image':filenames,'Caption' : captions})

        caption_csv = os.path.join(captions_directory_path,'captions.csv')
        captions_df.to_csv(caption_csv)

        logger.info(f"captions.csv successfully generated! in {captions_directory_path} directory for {set_type} set")

   
    def get_ROIs(self,set_type = 'train'):
        
        '''
        
        Create a ROI directory for storing the ROIs of Images

        '''

        roi_count = 0
        image_count = 0
        meta_data = None
        file_prefixes = None
        roi_directory_path = None

        if set_type == 'train':
            meta_data = pd.read_csv(self.TRAIN_META_DATA_FILE_PATH)
            file_prefixes = meta_data.loc[:,"File-Prefix"].values
            roi_directory_path = Path(f"Artifacts/{set_type}/roi")

        elif set_type == 'validation':
            meta_data = pd.read_csv(self.VALIDATION_META_DATA_FILE_PATH)
            file_prefixes = meta_data.loc[:,"File-Prefix"].values 
            roi_directory_path = Path(f"Artifacts/{set_type}/roi")

        
        os.makedirs(roi_directory_path,exist_ok = True)
        remove_files(roi_directory_path.as_posix())

        for file_prefix in tqdm(file_prefixes):

            image_count+=1

            image_path = Path(f"Artifacts/{set_type}/images/{file_prefix}.png")
            annotation_path = Path(f"Artifacts/{set_type}/annotations/{file_prefix}.xml")

            with open(annotation_path,'r') as f:
                data = f.read()
            

            original_img = cv2.imread(image_path.as_posix())
            annot = BeautifulSoup(data,'xml')

            xmin = int(annot.find('xmin').text)
            ymin = int(annot.find('ymin').text)
            xmax = int(annot.find('xmax').text)
            ymax = int(annot.find('ymax').text)


            scaled_img = cv2.resize(original_img,(224,224))
            scaled_xmin,scaled_ymin,scaled_xmax,scaled_ymax = self.scale_bbox(original_img.shape,(xmin,ymin,xmax,ymax),scaled_img.shape)

            roi = scaled_img[scaled_ymin:scaled_ymax,scaled_xmin:scaled_xmax]

            if roi.shape[0]==0 or roi.shape[1]==0 :
                corrupt_roi.append(file_prefix)
                continue

            save_img = os.path.join(roi_directory_path,file_prefix+'.png')

            cv2.imwrite(save_img,roi)
            roi_count +=1

        logger.info(f"{roi_count} appropriate ROI's generated out of {image_count} images in {roi_directory_path} for {set_type} set" )
        


    def get_bb_annoatation(self,set_type = 'train'):

        '''
        
            Get the all the BB annotations in the annotations.txt file
        
        '''

        save_directory_path = Path(f"Artifacts/{set_type}/BB_annotations")
        annotation_directory_path = Path(f"Artifacts/{set_type}/annotations/*")


        os.makedirs(save_directory_path,exist_ok = True)
        remove_files(save_directory_path.as_posix())

        annotations_paths = glob(annotation_directory_path.as_posix())
        
        annotations_paths = [path for path in annotations_paths if path.split('/')[-1].split('.')[0] not in corrupt_roi ]


        for annot_path in tqdm(annotations_paths):

            filename = annot_path.split('/')[-1].split('.')[0]

            if filename in corrupt_roi:
                continue

            with open(annot_path,'r') as f:
                data = f.read()

            a = BeautifulSoup(data,'xml')

            xmin = int(a.find('xmin').text)
            ymin = int(a.find('ymin').text)
            xmax = int(a.find('xmax').text)
            ymax = int(a.find('ymax').text)

            height = int(a.find('height').text)
            width = int(a.find('width').text)
            depth = int(a.find('depth').text)

            scaled_xmin,scaled_ymin,scaled_xmax,scaled_ymax = self.scale_bbox((height,width,depth),(xmin,ymin,xmax,ymax),(224,224,3))

            annots = ','.join([filename+'.txt',str(scaled_xmin),str(scaled_ymin),str(scaled_xmax),str(scaled_ymax),'\n'])

            with open(save_directory_path.as_posix()+'/annotations.txt','a') as annot_file:
                annot_file.write(annots)


        f.close()
        annot_file.close()

        logger.info(f"Annotations.txt successfully generated in {save_directory_path} for {set_type} set")        


    def prepare_data(self):

        logger.info("Started preparing Data for <<Training set>>")
        self.get_ROIs(set_type = 'train')
        self.get_captions(set_type = 'train')
        self.get_bb_annoatation(set_type = 'train')
        logger.info("Completed preparing Data for <<Training set>>")

        logger.info("Started preparing Data for <<Validation set>>")
        self.get_ROIs(set_type = 'validation')
        self.get_captions(set_type = 'validation')
        self.get_bb_annoatation(set_type = 'validation')
        logger.info("Completed preparing Data for <<Validation set>>")


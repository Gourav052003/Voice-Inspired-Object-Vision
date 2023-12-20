from Logger import logger
from Utils import save_as_pickle

from tqdm import tqdm
from glob import glob
from pathlib import Path
from keras import Sequential
from keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.applications.vgg19 import VGG19
from keras.preprocessing.sequence import pad_sequences

import os
import cv2
import numpy as np
import pandas as pd


class FeatureExtraction:

    def __init__(self):
        ...

    def get_tokenizer(self,text):

        logger.info(f"Building Tokenizer...")
        tokenizer = Tokenizer(oov_token = '<OOV>')
        tokenizer.fit_on_texts(text)
        save_as_pickle('Artifacts/tokenizer.pkl',tokenizer)
        logger.info(f"Tokenizer saved at Artifacts/tokenizer.pkl")

        return tokenizer  


    def get_text_sequences(self,tokenizer,text):

        logger.info(f"Building Text Sequences...")
        sequences = tokenizer.texts_to_sequences(text)
        logger.info(f"Padding Sequences with 100 max length...")
        padded_sequences = pad_sequences(sequences = sequences,maxlen = 100,padding = "post")
        
        return padded_sequences


    def standardize_bb(self,bb_labels):

        logger.info(f"Standardizing BB annotations label...")

        bb_df = pd.DataFrame(bb_labels)
        sc = StandardScaler()
        standardized_bb_labels = sc.fit_transform(bb_df)
        save_as_pickle("Artifacts/StandardScaler.pkl",sc)
        logger.info(f"Standardizer saved at Artifacts/StandardScaler.pkl")

        return standardized_bb_labels 


    def get_image_feature(self,images_path,set_type = 'train'):
        
        logger.info(f"Getting Image features using VGG19")
        roi_path = Path(f"Artifacts/{set_type}/roi")
        roi_valid_files = os.listdir(roi_path)

        logger.info(f"Getting Appropriate {set_type} images for feature extraction..")
        roi_valid_file_prefixes = [file.split('.')[0] for file in roi_valid_files]

        vgg_model = VGG19(include_top = False)
        model = Sequential([vgg_model])
        image_features = []

        images = glob(images_path)

        for img_path in tqdm(images):

            filename = img_path.split('/')[-1].split('.')[0]

            if filename not in roi_valid_file_prefixes:
                continue

            img = cv2.imread(img_path)
            img = cv2.resize(img,(224,224))

            x,y,z = img.shape

            reshaped_img = np.reshape(img,(1,x,y,z))

            features = model.predict(reshaped_img)

            image_features.append(features)

        logger.info(f"Image Feature extraction Completed!")

        return np.array(image_features)  


    def get_data_features(self,set_type = 'train'):

        image_path = Path(f"Artifacts/{set_type}/images/*")
        caption_csv = Path(f"Artifacts/{set_type}/captions/captions.csv")
        BB_file = Path(f"Artifacts/{set_type}/BB_annotations/annotations.txt")

        bb_labels = []

        logger.info(f"Getting Captions features...")
        text_data = pd.read_csv(caption_csv)
        captions = text_data['Caption'].values.tolist()

        tokenizer = self.get_tokenizer(captions)
        text_sequences = self.get_text_sequences(tokenizer,captions)
        logger.info(f"Captions feature extraction completed!")

        logger.info(f"Getting Image features...")
        image_features = self.get_image_feature(image_path.as_posix())
        logger.info(f"Images feature extraction completed!")


        logger.info(f"Getting BB annotations features...")
        with open(BB_file.as_posix()) as f:
            bb_annotations = f.readlines()

        for annotation in bb_annotations:
            
            xmin = int(annotation.split(',')[1:5][0])
            ymin = int(annotation.split(',')[1:5][1])
            xmax = int(annotation.split(',')[1:5][2])
            ymax = int(annotation.split(',')[1:5][3])

            bb_labels.append([xmin,ymin,xmax,ymax])

        bb_labels =  np.array(bb_labels)
        bb_labels = self.standardize_bb(bb_labels)
        logger.info(f"BB Annotations feature extraction completed!")

        return image_features,text_sequences,bb_labels

   

    def extract_features(self):

        logger.info(f"Started Extracting Training data features ....")
        train_image_features,train_text_sequences,train_bb_labels = self.get_data_features(set_type = 'train')

        save_as_pickle('Artifacts/train/image_features.pkl',train_image_features)
        logger.info(f"Train Image_features saved at Artifacts/train/image_features.pkl")

        save_as_pickle('Artifacts/train/text_sequences.pkl',train_text_sequences)
        logger.info(f"Train Image_features saved at Artifacts/train/text_sequences.pkl")
        
        save_as_pickle('Artifacts/train/bb_labels.pkl',train_bb_labels)
        logger.info(f"Train BB_labels features saved at Artifacts/train/bb_labels.pkl")

        logger.info(f"Training data feature extraction completed!")


        logger.info(f"Started Extracting Validation data features ....")
        validation_image_features,validation_text_sequences,validation_bb_labels = self.get_data_features(set_type = 'validation')

        save_as_pickle('Artifacts/validation/image_features.pkl',validation_image_features)
        logger.info(f"Validation Image_features saved at Artifacts/validation/image_features.pkl")
        
        save_as_pickle('Artifacts/validation/text_sequences.pkl',validation_text_sequences)
        logger.info(f"Validation text_sequences saved at Artifacts/validation/text_sequences.pkl")
        
        save_as_pickle('Artifacts/validation/bb_labels.pkl',validation_bb_labels)
        logger.info(f"Validation bb_labels saved at Artifacts/validation/bb_labels.pkl")
        
        logger.info(f"Validation data feature extraction completed!")



        


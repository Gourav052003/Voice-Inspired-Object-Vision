from Logger import logger
from Entities.entity import DataValidationConfig

from box import ConfigBox
from sklearn.model_selection import train_test_split

import os
import shutil
import pandas as pd



class DataValidation:

    def __init__(self,config:DataValidationConfig):

        self.SOURCE_DATASET_PATHS = ConfigBox({
                       'images':config.IMAGES_DATASET_PATH,
                       'annotations':config.ANNOTATIONS_DATASET_PATH
                })

        self.VALIDATION_DIRECTORIES = [ config.TRAIN_DATA_FILE_PATH,
                                        config.VALIDATION_DATA_FILE_PATH,
                                        config.TEST_DATA_FILE_PATH
                                    ]
       
        self.META_DATA_FILE_PATH = config.META_DATA_FILE_PATH

     
    def train_validation_test_splitting(self):

        meta_data_csv = pd.read_csv(self.META_DATA_FILE_PATH)

        train,test = train_test_split(meta_data_csv,test_size = 0.2,shuffle = True)
        train,validation = train_test_split(train,test_size = 0.2,shuffle = True)

        return train,validation,test



    def copy_to(self,data,destination_directory):

        file_prefixes = data.loc[:,"File-Prefix"].values
        pd.DataFrame({"File-Prefix":file_prefixes}).to_csv(os.path.join(destination_directory,'Meta-Data.csv'))

        images_destination_directory = os.path.join(destination_directory,"images")
        annotations_destination_directory = os.path.join(destination_directory,"annotations")

        os.makedirs(images_destination_directory,exist_ok=True)
        os.makedirs(annotations_destination_directory,exist_ok=True)

        for file_prefix in file_prefixes:

            images_file_path = os.path.join(self.SOURCE_DATASET_PATHS.images,f"{file_prefix}.png")
            annotations_file_path = os.path.join(self.SOURCE_DATASET_PATHS.annotations,f"{file_prefix}.xml")

            shutil.copy2(images_file_path,images_destination_directory)
            shutil.copy2(annotations_file_path,annotations_destination_directory)



    def execute_splitting(self,train,validation,test):

        for validation_directory in self.VALIDATION_DIRECTORIES:

            os.makedirs(validation_directory,exist_ok = True) # To handle missing directory on first run of code
            shutil.rmtree(validation_directory)
            os.makedirs(validation_directory,exist_ok = True)
            
        self.copy_to(train,self.VALIDATION_DIRECTORIES[0])
        logger.info("Train set is now ready!")
       
        self.copy_to(validation,self.VALIDATION_DIRECTORIES[1])
        logger.info("Validation set is now ready!")

        self.copy_to(test,self.VALIDATION_DIRECTORIES[2])
        logger.info("Test set is now ready!")


    def validate_data(self):

        train,validation,test = self.train_validation_test_splitting()
        self.execute_splitting(train,validation,test)
       
            


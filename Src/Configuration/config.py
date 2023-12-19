from Constant import CONFIG_FILE_PATH,PARAMS_FILE_PATH,DOWNLOAD_URL
from Utils import read_yaml
from Entities.entity import (DataIngestionConfig,
                            DataValidationConfig,
                            DataPreparationConfig)


class ConfigurationManager:

    def __init__(self):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)


    def get_data_ingestion_config(self)->DataIngestionConfig:

        config = self.config.DataIngestion

        data_ingestion_config = DataIngestionConfig(

            ZIP_FILENAME = config.ZIP_FILENAME,
            UNZIP_DIRECTORY = config.UNZIP_DIRECTORY,
            DOWNLOAD_URL= DOWNLOAD_URL 

        )

        return data_ingestion_config


    def get_data_validation_config(self)->DataValidationConfig:

        config = self.config.DataValidation 

        data_validation_config = DataValidationConfig(

            IMAGES_DATASET_PATH = config.IMAGES_DATASET_PATH,
            ANNOTATIONS_DATASET_PATH = config.ANNOTATIONS_DATASET_PATH,
            META_DATA_FILE_PATH = config.META_DATA_FILE_PATH,
            TRAIN_DATA_FILE_PATH = config.TRAIN_DATA_FILE_PATH,
            VALIDATION_DATA_FILE_PATH = config.VALIDATION_DATA_FILE_PATH,
            TEST_DATA_FILE_PATH = config.TEST_DATA_FILE_PATH

        )

        return data_validation_config


    def get_data_preparation_config(self)->DataPreparationConfig:

        config = self.config.DataPreparation

        data_preparation_config = DataPreparationConfig(

            TRAIN_META_DATA_FILE_PATH = config.TRAIN_META_DATA_FILE_PATH,
            VALIDATION_META_DATA_FILE_PATH = config.VALIDATION_META_DATA_FILE_PATH,
                       
        )

        return data_preparation_config   



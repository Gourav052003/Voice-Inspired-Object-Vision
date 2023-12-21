from Logger import logger
from Constant import CONFIG_FILE_PATH,PARAMS_FILE_PATH,DOWNLOAD_URL
from Utils import read_yaml
from Entities.entity import (DataIngestionConfig,
                            DataValidationConfig,
                            DataPreparationConfig,
                            FeatureExtractionConfig,
                            ModelArchitectureConfig,
                            ModelCallbacksConfig,
                            ModelTrainingConfig)

from box import ConfigBox                            


class ConfigurationManager:

    def __init__(self):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)


    def get_data_ingestion_config(self)->DataIngestionConfig:

        logger.info("Getting Data Ingestion Configuration...")

        config = self.config.DataIngestion

        data_ingestion_config = DataIngestionConfig(

            ZIP_FILENAME = config.ZIP_FILENAME,
            UNZIP_DIRECTORY = config.UNZIP_DIRECTORY,
            DOWNLOAD_URL= DOWNLOAD_URL 

        )

        return data_ingestion_config


    def get_data_validation_config(self)->DataValidationConfig:

        logger.info("Getting Data Validation Configuration...")

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

        logger.info("Getting Data Preparation Configuration...")

        config = self.config.DataPreparation

        data_preparation_config = DataPreparationConfig(

            TRAIN_META_DATA_FILE_PATH = config.TRAIN_META_DATA_FILE_PATH,
            VALIDATION_META_DATA_FILE_PATH = config.VALIDATION_META_DATA_FILE_PATH,
                       
        )

        return data_preparation_config   

    def get_feature_extraction_config(self)-> FeatureExtractionConfig:

        logger.info("Getting Feature Extraction Configuration...")

        config = self.config.FeatureExtraction
        params = self.params.FeatureExtraction

        feature_extraction_config = FeatureExtractionConfig(

            SET_TYPE = ConfigBox(params.SET_TYPE),
            PICKLE_TRAIN_IMAGES_FEATURES_PATH  = config.PICKLE_TRAIN_IMAGES_FEATURES_PATH,
            PICKLE_TRAIN_BB_FEATURES_PATH  = config.PICKLE_TRAIN_BB_FEATURES_PATH,
            PICKLE_TRAIN_TEXT_SEQUENCES_FEATURES_PATH  = config.PICKLE_TRAIN_TEXT_SEQUENCES_FEATURES_PATH,
            PICKLE_VALIDATION_IMAGES_FEATURES_PATH  = config.PICKLE_VALIDATION_IMAGES_FEATURES_PATH,
            PICKLE_VALIDATION_BB_FEATURES_PATH  = config.PICKLE_VALIDATION_BB_FEATURES_PATH,
            PICKLE_VALIDATION_TEXT_SEQUENCES_FEATURES_PATH  = config.PICKLE_VALIDATION_TEXT_SEQUENCES_FEATURES_PATH
        )

        return feature_extraction_config

    def get_model_architecture_config(self)->ModelArchitectureConfig:

        logger.info("Getting Model Architecture Configuration...")

        config = self.config.ModelArchitecture
        params = self.params.ModelArchitecture

        model_architecture_config = ModelArchitectureConfig(

            SAVE_MODEL_PATH = config.SAVE_MODEL_PATH,

            FEATURE_SIZE = params.FEATURE_SIZE,
            TEXT_SEQUENCE_INPUT_LENGTH = params.TEXT_SEQUENCE_INPUT_LENGTH,
            EMBEDDING_INPUT_DIMS = params.EMBEDDING_INPUT_DIMS,
            EMBEDDING_OUTPUT_DIMS = params.EMBEDDING_OUTPUT_DIMS,
            LEARNING_RATE = params.LEARNING_RATE,
            LOSS = params.LOSS
            

        )

        return model_architecture_config


    def get_model_callbacks_config(self)->ModelCallbacksConfig: 

        logger.info("Getting Model Callbacks Configuration...")


        config = self.config.ModelCallbacks
        params = self.params.ModelCallbacks

        model_callbacks_config = ModelCallbacksConfig(


            BEST_MODEL_PATH = config.BEST_MODEL_PATH,
            PICKLE_MODEL_CALLBACKS = config.PICKLE_MODEL_CALLBACKS,

            SAVE_BEST_ONLY = params.SAVE_BEST_ONLY
        ) 

        return model_callbacks_config


    def get_model_training_config(self)->ModelTrainingConfig:

        logger.info(f"Getting Model Training configuration...")

        config = self.config.ModelTraining
        params = self.params.ModelTraining

        model_training_config = ModelTrainingConfig(

            EPOCHS = params.EPOCHS,
            BATCH_SIZE  = params.BATCH_SIZE,
            VALIDATION_BATCH_SIZE = params.VALIDATION_BATCH_SIZE,  

            SAVE_MODEL_PATH = config.SAVE_MODEL_PATH,
            PICKLE_MODEL_CALLBACKS = config.PICKLE_MODEL_CALLBACKS, 
            BEST_MODEL_PATH = config.BEST_MODEL_PATH,
            MODEL_HISTORY_PICKLE = config.MODEL_HISTORY_PICKLE,
            PICKLE_TRAIN_IMAGES_FEATURES_PATH = config.PICKLE_TRAIN_IMAGES_FEATURES_PATH, 
            PICKLE_TRAIN_BB_FEATURES_PATH = config.PICKLE_TRAIN_BB_FEATURES_PATH, 
            PICKLE_TRAIN_TEXT_SEQUENCES_FEATURES_PATH = config.PICKLE_TRAIN_TEXT_SEQUENCES_FEATURES_PATH,
            PICKLE_VALIDATION_IMAGES_FEATURES_PATH = config.PICKLE_VALIDATION_IMAGES_FEATURES_PATH, 
            PICKLE_VALIDATION_BB_FEATURES_PATH = config.PICKLE_VALIDATION_BB_FEATURES_PATH, 
            PICKLE_VALIDATION_TEXT_SEQUENCES_FEATURES_PATH = config.PICKLE_VALIDATION_TEXT_SEQUENCES_FEATURES_PATH  
        )

        return model_training_config

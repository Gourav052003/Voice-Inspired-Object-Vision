import os
import sys

path = os.path.abspath("Src")
sys.path.append(path)

from Logger import logger
from Configuration.config import ConfigurationManager
from Components.Data_Validation import DataValidation

STAGE_NAME = "Data Validation"

class DataValidationTrainingPipeline:

    def __init__(self):
        pass

    def start(self):

        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_data()
      

if __name__ == "__main__":

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        Data_validation_training_pipeline = DataValidationTrainingPipeline()
        Data_validation_training_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
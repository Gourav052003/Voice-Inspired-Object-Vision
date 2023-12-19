import os
import sys

path = os.path.abspath("Src")
sys.path.append(path)

from Logger import logger
from Configuration.config import ConfigurationManager
from Components.Data_Preparation import DataPreparation

STAGE_NAME = "Data Preparation"

class DataPreparationTrainingPipeline:

    def __init__(self):
        pass

    def start(self):
        config = ConfigurationManager()
        data_preparation_config = config.get_data_preparation_config()
        data_preparation = DataPreparation(config = data_preparation_config)
        data_preparation.prepare_data()


if __name__ == "__main__":

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        Data_preparation_training_pipeline = DataPreparationTrainingPipeline()
        Data_preparation_training_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e        



import os
import sys

path = os.path.abspath("Src")
sys.path.append(path)

from Logger import logger
from Configuration.config import ConfigurationManager
from Components.Model_Training import ModelTraining


STAGE_NAME = "Model Training"

class ModelTrainingPipeline:

    def __init__(self):
        pass

    def start(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        model_trainer = ModelTraining(config = model_training_config)
        model_trainer.train_model()

if __name__ == "__main__":

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_training_pipeline = ModelTrainingPipeline()
        model_training_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

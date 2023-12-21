import os
import sys

path = os.path.abspath("Src")
sys.path.append(path)

from Logger import logger
from Configuration.config import ConfigurationManager
from Components.Model_Architecture import ModelArchitecture

STAGE_NAME = "Model Architecture Development"

class ModelArchitectureTrainingPipeline:

    def __init__(self):
        pass


    def start(self):

        config = ConfigurationManager()
        model_architecture_config = config.get_model_architecture_config()
        model_architecture = ModelArchitecture(config = model_architecture_config)
        model_architecture.Develop_Model_architecture()


if __name__ == "__main__":

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_architecture_development_pipeline = ModelArchitectureTrainingPipeline()
        model_architecture_development_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e  
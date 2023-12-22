import os
import sys

path = os.path.abspath("Src")
sys.path.append(path)

from Logger import logger
from Configuration.config import ConfigurationManager
from Components.Model_Testing import ModelTesting

STAGE_NAME = "Model Testing"

class ModelTestingPipeline:

    def __init__(self):
        pass

    def start(self):

        config = ConfigurationManager()
        model_testing_config = config.get_model_testing_config()
        model_tester = ModelTesting(config = model_testing_config)
        model_tester.predict()


if __name__ == "__main__":

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_testing_pipeline = ModelTestingPipeline()
        model_testing_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e        




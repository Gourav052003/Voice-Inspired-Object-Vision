import os
import sys

path = os.path.abspath("Src")
sys.path.append(path)

from Logger import logger
from Configuration.config import ConfigurationManager
from Components.Model_Callbacks import ModelCallbacks

STAGE_NAME = "Model Callbacks"

class ModelCallbacksTrainingPipeline:

    def __init__(self):
        pass

    def start(self):

        config = ConfigurationManager()
        model_callbacks_config = config.get_model_callbacks_config()
        model_callbacks = ModelCallbacks(config = model_callbacks_config)
        model_callbacks.get_model_callbacks()



if __name__ == "__main__":

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_callbacks_training_pipeline = ModelCallbacksTrainingPipeline()
        model_callbacks_training_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e  

        


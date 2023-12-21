import os
import sys

path = os.path.abspath("Src")
sys.path.append(path)

from Logger import logger
from Configuration.config import  ConfigurationManager
from Components.Feature_Extraction import FeatureExtraction

STAGE_NAME = "Feature Extraction"

class FeatureExtractionTrainingPipeline:

    def __init__(self):
        pass

    def start(self):

        config = ConfigurationManager()
        feature_extraction_config = config.get_feature_extraction_config()
        feature_extraction = FeatureExtraction(config = feature_extraction_config)
        feature_extraction.extract_features()

if __name__ == "__main__":

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        Feature_extractiion_training_pipeline = FeatureExtractionTrainingPipeline()
        Feature_extractiion_training_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e  



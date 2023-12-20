import os
import sys

path = os.path.abspath("Src")
sys.path.append(path)

from Logger import logger
from Components.Feature_Extraction import FeatureExtraction

STAGE_NAME = "Feature Extraction"

class FeatureExtractionTrainingPipeline:

    def __init__(self):
        pass

    def start(self):

        feature_extraction = FeatureExtraction()
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



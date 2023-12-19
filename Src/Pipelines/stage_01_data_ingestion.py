import os
import sys
from pathlib import Path

path = os.path.abspath(Path("Src"))
sys.path.append(path)

from Logger import logger
from Configuration.config import ConfigurationManager
from Components.Data_Ingestion import DataIngestion

STAGE_NAME = "Data Ingestion"

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass

    def start(self):

        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.Ingest_Data()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        Data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
        Data_ingestion_training_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
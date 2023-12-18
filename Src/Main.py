from Logger import logger
from Pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

if __name__ == '__main__':
    
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        Data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
        Data_ingestion_training_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e 

from Logger import logger
from Pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Pipelines.stage_02_data_validation import DataValidationTrainingPipeline
from Pipelines.stage_03_data_preparation import DataPreparationTrainingPipeline

STAGE_NAME = "Data Ingestion"

if __name__ == '__main__':
    
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        # Data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
        # Data_ingestion_training_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e 


    STAGE_NAME = "Data Validation"        

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        # Data_validation_training_pipeline = DataValidationTrainingPipeline()
        # Data_validation_training_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

    STAGE_NAME = "Data Preparation"  

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        # Data_preparation_training_pipeline = DataPreparationTrainingPipeline()
        # Data_preparation_training_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e            




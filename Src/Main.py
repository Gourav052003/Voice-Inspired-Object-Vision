from Logger import logger
from Pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Pipelines.stage_02_data_validation import DataValidationTrainingPipeline
from Pipelines.stage_03_data_preparation import DataPreparationTrainingPipeline
from Pipelines.stage_04_feature_extraction import FeatureExtractionTrainingPipeline
from Pipelines.stage_05_model_architecture import ModelArchitectureTrainingPipeline
from Pipelines.stage_06_model_callbacks import ModelCallbacksTrainingPipeline



if __name__ == '__main__':

    STAGE_NAME = "Data Ingestion"
    
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

    STAGE_NAME = "Feature Extraction"  


    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        # Feature_extractiion_training_pipeline = FeatureExtractionTrainingPipeline()
        # Feature_extractiion_training_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e  


    STAGE_NAME = "Model Architecture Developement"

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        # model_architecture_development_pipeline = ModelArchitectureTrainingPipeline()
        # model_architecture_development_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


    STAGE_NAME = "Model Callbacks"

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        # model_callbacks_training_pipeline = ModelCallbacksTrainingPipeline()
        # model_callbacks_training_pipeline.start()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e      


    
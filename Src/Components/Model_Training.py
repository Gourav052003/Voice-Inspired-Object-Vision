from Logger import logger
from Utils import load_pickle,save_as_pickle
from Entities.entity import ModelTrainingConfig


class ModelTraining:

    def __init__(self,config:ModelTrainingConfig):

        self.EPOCHS = config.EPOCHS
        self.BATCH_SIZE  = config.BATCH_SIZE
        self.VALIDATION_BATCH_SIZE = config.VALIDATION_BATCH_SIZE  

        self.SAVE_MODEL_PATH = config.SAVE_MODEL_PATH
        self.PICKLE_MODEL_CALLBACKS = config.PICKLE_MODEL_CALLBACKS 
        self.BEST_MODEL_PATH = config.BEST_MODEL_PATH
        self.MODEL_HISTORY_PICKLE = config.MODEL_HISTORY_PICKLE

        self.PICKLE_TRAIN_IMAGES_FEATURES_PATH = config.PICKLE_TRAIN_IMAGES_FEATURES_PATH
        self.PICKLE_TRAIN_TEXT_SEQUENCES_FEATURES_PATH = config.PICKLE_TRAIN_TEXT_SEQUENCES_FEATURES_PATH
        self.PICKLE_TRAIN_BB_FEATURES_PATH = config.PICKLE_TRAIN_BB_FEATURES_PATH

        self.PICKLE_VALIDATION_IMAGES_FEATURES_PATH = config.PICKLE_VALIDATION_IMAGES_FEATURES_PATH
        self.PICKLE_VALIDATION_TEXT_SEQUENCES_FEATURES_PATH = config.PICKLE_VALIDATION_TEXT_SEQUENCES_FEATURES_PATH
        self.PICKLE_VALIDATION_BB_FEATURES_PATH = config.PICKLE_VALIDATION_BB_FEATURES_PATH


    def load_data(self):

        logger.info("Loading Training Data...")
        train_image_features = load_pickle(self.PICKLE_TRAIN_IMAGES_FEATURES_PATH)
        train_text_sequences_features = load_pickle(self.PICKLE_TRAIN_TEXT_SEQUENCES_FEATURES_PATH) 
        train_bb_features = load_pickle(self.PICKLE_TRAIN_BB_FEATURES_PATH)
        logger.info("Training Data Successfully Loaded!")

        logger.info("Loading Validation Data...")
        validation_image_features = load_pickle(self.PICKLE_VALIDATION_IMAGES_FEATURES_PATH)
        validation_text_sequences_features = load_pickle(self.PICKLE_VALIDATION_TEXT_SEQUENCES_FEATURES_PATH) 
        validation_bb_features = load_pickle(self.PICKLE_VALIDATION_BB_FEATURES_PATH) 
        logger.info("Validation Data Successfully Loaded!")

        train_x = [train_image_features,train_text_sequences_features]
        train_y = train_bb_features
      
        validation_x = [validation_image_features,validation_text_sequences_features]
        validation_y = validation_bb_features
     
        return train_x,train_y,validation_x,validation_y


    def train_model(self):

        train_x,train_y,validation_x,validation_y = self.load_data()

        logger.info(f"Loading Model from {self.SAVE_MODEL_PATH} ...")

        model = load_pickle(self.SAVE_MODEL_PATH)
        logger.info(f"Model Successfully loaded!")

        logger.info(f"Model Callbacks loading from {self.PICKLE_MODEL_CALLBACKS}...")
        model_callbacks = load_pickle(self.PICKLE_MODEL_CALLBACKS)
        logger.info(f"Model Callbacks Successfully loaded!")


        logger.info(f"Model Training Started...")
        model_history = model.fit(x = train_x, y = train_y, epochs = self.EPOCHS, batch_size = self.BATCH_SIZE,
                    validation_data = (validation_x,validation_y), validation_batch_size = self.VALIDATION_BATCH_SIZE,
                    callbacks = model_callbacks
                    ) 

        logger.info(f"Model training Completed!")
        logger.info(f"Best Model Saved at {self.BEST_MODEL_PATH}")                     
        save_as_pickle(self.MODEL_HISTORY_PICKLE,model_history)           
        logger.info(f"Model History saved at {self.MODEL_HISTORY_PICKLE}")
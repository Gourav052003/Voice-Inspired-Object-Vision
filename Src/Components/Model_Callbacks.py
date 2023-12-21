from Logger import logger
from Utils import save_as_pickle
from Entities.entity import ModelCallbacksConfig

from keras.callbacks import ModelCheckpoint




class ModelCallbacks:

    def __init__(self,config:ModelCallbacksConfig):

        self.BEST_MODEL_PATH = config.BEST_MODEL_PATH
        self.PICKLE_MODEL_CALLBACKS = config.PICKLE_MODEL_CALLBACKS
        self.SAVE_BEST_ONLY = config.SAVE_BEST_ONLY


    def get_model_callbacks(self):

        logger.info(f"Building Model Callbacks...")
        model_checkpoint = [ModelCheckpoint(save_best_only = True,filepath = 'Datasets/Traffic light BB/best_model.h5')]
        save_as_pickle(self.PICKLE_MODEL_CALLBACKS,model_checkpoint)
        logger.info(f"Model callbacks saved at {self.PICKLE_MODEL_CALLBACKS}")


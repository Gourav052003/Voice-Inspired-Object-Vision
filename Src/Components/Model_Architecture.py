from Logger import logger
from Utils import save_as_pickle
from Entities.entity import ModelArchitectureConfig

from keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Flatten,Dense,Input,Concatenate,Embedding,Reshape,Add

class ModelArchitecture:

    def __init__(self,config:ModelArchitectureConfig):
        self.SAVE_MODEL_PATH = config.SAVE_MODEL_PATH
        self.FEATURE_SIZE = config.FEATURE_SIZE
        self.TEXT_SEQUENCE_INPUT_LENGTH = config.TEXT_SEQUENCE_INPUT_LENGTH
        self.EMBEDDING_INPUT_DIMS = config.EMBEDDING_INPUT_DIMS
        self.EMBEDDING_OUTPUT_DIMS =config.EMBEDDING_OUTPUT_DIMS
        self.LEARNING_RATE = config.LEARNING_RATE
        self.LOSS = config.LOSS

    def hidden_layer(self,input_layer):
        Dense_1 = Dense(2,activation = 'tanh')(input_layer)
        Dense_2 = Dense(4,activation = 'tanh')(Dense_1)
        Dense_3 = Dense(6,activation = 'tanh')(Dense_2)
        Dense_4 = Dense(self.FEATURE_SIZE,activation = 'tanh')(Dense_3)

        return Dense_4

    def relational_neural_unit(self,input):
        r = Reshape((self.FEATURE_SIZE,2))(input)
        Dense_1 = Dense(1,activation='tanh')(r)
        flatten = Flatten()(Dense_1)

        return flatten

    def get_model(self):

        image_features_input_layer = Input(shape = (1,7,7,512), name = 'image_features_input_layer')

        reshape_image_features_layer = Reshape(target_shape = (1,7*7*512),
                                          name = 'reshape_image_features_layer')(image_features_input_layer)

        image_processsing_hidden_layer = self.hidden_layer(reshape_image_features_layer)

        text_sequences_input_layer = Input(shape = (self.TEXT_SEQUENCE_INPUT_LENGTH),name = 'text_sequences_input_layer')

        text_embeddings_layer = Embedding(input_dim = self.EMBEDDING_INPUT_DIMS,
                                          output_dim = self.EMBEDDING_OUTPUT_DIMS,
                                          input_length = (self.TEXT_SEQUENCE_INPUT_LENGTH),
                                          name = 'text_embeddings_layer')(text_sequences_input_layer)

        reshape_text_features_layer = Reshape(target_shape = (1,-1),name = 'reshape_text_features_layer')(text_embeddings_layer)
        text_processsing_hidden_layer = self.hidden_layer(reshape_text_features_layer)

        concatenation_layer = Concatenate(axis=-1,name = 'concatenation_layer')([image_processsing_hidden_layer,text_processsing_hidden_layer])
        relation_layer = self.relational_neural_unit(concatenation_layer)

        BB_processing_hidden_layer = self.hidden_layer(relation_layer)
        BB_prediction_hidden_layer = Dense(4)(BB_processing_hidden_layer)

        model = Model(inputs = [image_features_input_layer,text_sequences_input_layer],outputs = BB_prediction_hidden_layer)

        model.compile(optimizer = Adam(learning_rate= self.LEARNING_RATE),loss = self.LOSS)

        return model


    def Develop_Model_architecture(self):

        logger.info(f"Model Build in progress..")
        model = self.get_model()
        logger.info(f"Model Successfully Builted!")
        model.summary()
        save_as_pickle(self.SAVE_MODEL_PATH,model)
        logger.info(f"Model saved at {self.SAVE_MODEL_PATH}")




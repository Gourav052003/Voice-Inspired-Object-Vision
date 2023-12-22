from Logger import logger
from Utils import load_pickle
from Entities.entity import ModelTestingConfig 

from pathlib import Path
from keras.models import load_model
from keras import Sequential
from tensorflow.keras.applications.vgg19 import VGG19
from keras.preprocessing.sequence import pad_sequences

import os
import cv2
import time
import mimetypes
import numpy as np
import moviepy.video.io.ImageSequenceClip

class ModelTesting:

    def __init__(self,config:ModelTestingConfig):

        self.BEST_MODEL_PATH = config.BEST_MODEL_PATH
        self.PICKLE_TOKENIZER_PATH = config.PICKLE_TOKENIZER_PATH
        self.PICKLE_STANDARD_SCALER_PATH = config.PICKLE_STANDARD_SCALER_PATH
        self.SOURCE = config.SOURCE
        self.TEXT = config.TEXT
        self.SAVE_RESULTS_PATH = config.SAVE_RESULTS_PATH
    
    def get_text_sequences(self,tokenizer,text):

        sequences = tokenizer.texts_to_sequences(text)
        padded_sequences = pad_sequences(sequences = sequences,maxlen = 100,padding = "post")

        return padded_sequences

    def get_test_data(self,img,text,tokenizer):

        vgg_model = VGG19(include_top = False)
        feature_extactor_model = Sequential([vgg_model])

        img = cv2.resize(img,(224,224))
        x,y,z = img.shape

        reshaped_img = np.reshape(img,(1,x,y,z))
        img_features = feature_extactor_model.predict(reshaped_img)
        img_features = img_features.reshape((1,1,7,7,512))
        text_sequence = self.get_text_sequences(tokenizer,text)


        return img_features,text_sequence

    def source_image(self,source,model,text,standard_scaler,tokenizer):

        logger.info(f"Source is an <<Image>>!")
    
        img = cv2.imread(source)
       

        filename = os.path.split(source)[1]

        image_features,text_sequence = self.get_test_data(img,[text],tokenizer)
        prediction = model.predict([image_features,text_sequence])
        prediction = prediction[0]


        scaled_out_prediction = standard_scaler.inverse_transform(prediction.reshape(1,-1))

        height,width = img.shape[:2]
        height_factor = 224/height
        width_factor = 224/width

        xmin = round(scaled_out_prediction[0][0]/width_factor)
        ymin = round(scaled_out_prediction[0][1]/height_factor)
        xmax = round(scaled_out_prediction[0][2]/width_factor)
        ymax = round(scaled_out_prediction[0][3]/height_factor)


        bb_frame = cv2.rectangle(img,(xmin,ymax),(xmax,ymin),(255, 0, 0),2)

        save_directory_path = os.path.join(self.SAVE_RESULTS_PATH,"Images")
        os.makedirs(save_directory_path,exist_ok=True)
        cv2.imwrite(f"{save_directory_path}/{filename}",bb_frame)

        logger.info(f"Results saved at {save_directory_path}/{filename}")
        
        return bb_frame
    

    def source_video(self,source,model,text,standard_scaler,tokenizer):
        
        filename = os.path.split(source)[1]

        vid = cv2.VideoCapture(source)
        anyFrame = True
        video_frames = []
        height,width = None,None

        logger.info(f"Source is a <<Video>>!")

        while anyFrame:
            anyFrame,frame  = vid.read()


            image_features,text_sequence = self.get_test_data(frame,[text],tokenizer)
            prediction = model.predict([image_features,text_sequence])
            prediction = prediction[0]

            scaled_out_prediction = standard_scaler.inverse_transform(prediction.reshape(1,-1))

            height,width = frame.shape[:2]
            height_factor = 224/height
            width_factor = 224/width

            xmin = round(scaled_out_prediction[0][0]/width_factor)
            ymin = round(scaled_out_prediction[0][1]/height_factor)
            xmax = round(scaled_out_prediction[0][2]/width_factor)
            ymax = round(scaled_out_prediction[0][3]/height_factor)


            bb_frame = cv2.rectangle(frame,(xmin,ymax),(xmax,ymin),(255, 0, 0),2)
            bb_frame = cv2.cvtColor(bb_frame, cv2.COLOR_BGR2RGB)
            video_frames.append(bb_frame)
            print(xmin,ymin,xmax,ymax)

            cv2.imshow("Video show",bb_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break

        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(video_frames, fps=20)

        save_directory_path = os.path.join(self.SAVE_RESULTS_PATH,"Videos")
        os.makedirs(save_directory_path,exist_ok = True)
        clip.write_videofile(f"{save_directory_path}/Results_{filename}")
        logger.info(f"Results saved at {save_directory_path}/{filename}")



    def source_camera(self,model,text,standard_scaler,tokenizer):

        timestamp = time.ctime(time.time())
        timestamp = timestamp.split(" ")
        timestamp = "_".join(timestamp)
        timestamp = timestamp.split(":")
        timestamp = "_".join(timestamp)


        save_directory_path = os.path.join(self.SAVE_RESULTS_PATH,"Real-time")
        os.makedirs(save_directory_path,exist_ok = True)
        
        vid = cv2.VideoCapture(0)

        anyFrame = True
        video_frames = []

        while anyFrame:
            anyFrame,frame = vid.read()


            image_features,text_sequence = self.get_test_data(frame,[text],tokenizer)
            prediction = model.predict([image_features,text_sequence])
            prediction = prediction[0]


            scaled_out_prediction = standard_scaler.inverse_transform(prediction.reshape(1,-1))

            height,width = frame.shape[:2]
            height_factor = 224/height
            width_factor = 224/width

            xmin = round(scaled_out_prediction[0][0]/width_factor)
            ymin = round(scaled_out_prediction[0][1]/height_factor)
            xmax = round(scaled_out_prediction[0][2]/width_factor)
            ymax = round(scaled_out_prediction[0][3]/height_factor)


            bb_frame = cv2.rectangle(frame,(xmin,ymax),(xmax,ymin),(255, 0, 0),2)
            bb_frame = cv2.cvtColor(bb_frame, cv2.COLOR_BGR2RGB)
           
            video_frames.append(bb_frame)

            bb_frame = cv2.cvtColor(bb_frame, cv2.COLOR_RGB2BGR)
            cv2.imshow('frame', bb_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        vid.release()
        cv2.destroyAllWindows()
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(video_frames, fps=10)
        clip.write_videofile(f"{save_directory_path}/{timestamp}.mp4")
        logger.info(f"Results saved at {save_directory_path}/{timestamp}.mp4")




    def get_prediction(self,model,standard_scaler,tokenizer,text:str = None,source:Path=None):


        if text==None:
            logger.info("Text not Provided!")
            return

        if source==None:
            self.source_camera(model,text,standard_scaler,tokenizer)
            return

        filetype = mimetypes.guess_type(source)[0].split('/')[0]

        if filetype == 'image':
            bb_img = self.source_image(source,model,text,standard_scaler,tokenizer)
            return bb_img
        elif filetype == 'video':
            data = self.source_video(source,model,text,standard_scaler,tokenizer)
            return data
        

    def predict(self):
        
        logger.info(f"Loading Standard Scaler from {self.PICKLE_STANDARD_SCALER_PATH}")
        sc = load_pickle(self.PICKLE_STANDARD_SCALER_PATH)
        logger.info(f"Standard Scaler loaded!")

        logger.info(f"Loading Tokenizer from {self.PICKLE_TOKENIZER_PATH}")
        tk = load_pickle(self.PICKLE_TOKENIZER_PATH) 
        logger.info(f"Tokenizer loaded!")


        logger.info(f"Loading the Best model from {self.BEST_MODEL_PATH}")
        model = load_model(self.BEST_MODEL_PATH)
        logger.info(f"Best Model loaded!")


        logger.info(f"Proceeding with the Prediction...")
        # self.get_prediction(model = model,standard_scaler = sc,tokenizer = tk,text = self.TEXT,source = self.SOURCE)
        self.get_prediction(model = model,standard_scaler = sc,tokenizer = tk,text = self.TEXT)
        logger.info(f"Predictions Completed!")

        
from Logger import logger
from Entities.entity import DataIngestionConfig

import os
import zipfile
import gdown


class DataIngestion:

    def __init__(self,config:DataIngestionConfig):

        self.ZIP_FILENAME = config.ZIP_FILENAME
        self.UNZIP_DIRECTORY = config.UNZIP_DIRECTORY
        self.DOWNLOAD_URL = config.DOWNLOAD_URL

    def Ingest_Data(self):

        gdown.download(self.DOWNLOAD_URL,self.ZIP_FILENAME)

        os.makedirs(self.UNZIP_DIRECTORY,exist_ok=True)

        with zipfile.ZipFile(self.ZIP_FILENAME, 'r') as zip_ref:
            zip_ref.extractall(self.UNZIP_DIRECTORY)    

      
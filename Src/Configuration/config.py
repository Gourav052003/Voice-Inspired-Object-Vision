from Constant import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from Utils import read_yaml
from Entities.entity import (DataIngestionConfig)


class ConfigurationManager:

    def __init__(self):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)


    def get_data_ingestion_config(self)->DataIngestionConfig:
        





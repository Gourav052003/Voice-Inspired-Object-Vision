from dataclasses import dataclass
from pathlib import Path
from box import ConfigBox
from xmlrpc.client import Boolean

@dataclass(frozen=True)
class DataIngestionConfig:
    ZIP_FILENAME : Path
    UNZIP_DIRECTORY : Path
    DOWNLOAD_URL : str

@dataclass(frozen=True)
class DataValidationConfig:
    IMAGES_DATASET_PATH : Path
    ANNOTATIONS_DATASET_PATH : Path
    META_DATA_FILE_PATH : Path 
    TRAIN_DATA_FILE_PATH : Path 
    VALIDATION_DATA_FILE_PATH : Path 
    TEST_DATA_FILE_PATH : Path 

@dataclass(frozen=True)
class DataPreparationConfig:
    TRAIN_META_DATA_FILE_PATH: Path 
    VALIDATION_META_DATA_FILE_PATH: Path 

@dataclass(frozen=True)
class FeatureExtractionConfig:
    SET_TYPE : ConfigBox
    PICKLE_TRAIN_IMAGES_FEATURES_PATH : Path
    PICKLE_TRAIN_BB_FEATURES_PATH : Path
    PICKLE_TRAIN_TEXT_SEQUENCES_FEATURES_PATH : Path
    PICKLE_VALIDATION_IMAGES_FEATURES_PATH : Path
    PICKLE_VALIDATION_BB_FEATURES_PATH : Path
    PICKLE_VALIDATION_TEXT_SEQUENCES_FEATURES_PATH : Path

@dataclass(frozen=True)
class ModelArchitectureConfig:
    SAVE_MODEL_PATH:Path
    FEATURE_SIZE: int
    TEXT_SEQUENCE_INPUT_LENGTH:int
    EMBEDDING_INPUT_DIMS : int
    EMBEDDING_OUTPUT_DIMS : int
    LEARNING_RATE: float
    LOSS : str 

@dataclass(frozen=True)
class ModelCallbacksConfig:
    BEST_MODEL_PATH:Path
    PICKLE_MODEL_CALLBACKS:Path
    SAVE_BEST_ONLY: bool

@dataclass(frozen = True)
class ModelTrainingConfig:

    EPOCHS: int
    BATCH_SIZE : int
    VALIDATION_BATCH_SIZE: int 
    SAVE_MODEL_PATH : Path 
    PICKLE_MODEL_CALLBACKS: Path
    BEST_MODEL_PATH: Path
    MODEL_HISTORY_PICKLE : Path
    PICKLE_TRAIN_IMAGES_FEATURES_PATH : Path
    PICKLE_TRAIN_BB_FEATURES_PATH : Path
    PICKLE_TRAIN_TEXT_SEQUENCES_FEATURES_PATH : Path
    PICKLE_VALIDATION_IMAGES_FEATURES_PATH : Path
    PICKLE_VALIDATION_BB_FEATURES_PATH : Path
    PICKLE_VALIDATION_TEXT_SEQUENCES_FEATURES_PATH : Path 


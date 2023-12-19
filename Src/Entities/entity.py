from dataclasses import dataclass
from pathlib import Path

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


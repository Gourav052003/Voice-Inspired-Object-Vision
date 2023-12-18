from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    ZIP_FILENAME : Path
    UNZIP_DIRECTORY : Path
    DOWNLOAD_URL : str

from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from Logger import logger
from pathlib import Path
from glob import glob
from pickle import load,dump
import yaml
import os


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e



def remove_files(dir_name):

    p = glob(dir_name+'/*')

    if len(p)!=0:

        for files in p:
            f = files

            try:
                os.remove(f)
            except:
                logger.info(f"{f} does not exists")
                return

            logger.info(f"{f} file removed")


def save_as_pickle(fname,data):
  pfile = open(fname,'ab')
  dump(data,pfile)
  pfile.close()

def load_pickle(fname):
  pfile = open(fname,'rb')
  data = load(pfile)
  pfile.close()
  return data  
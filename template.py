from genericpath import exists
from pathlib import Path
import logging 
import os
import sys

logging.basicConfig(
                    level = logging.INFO,
                    format='[%(asctime)s: %(levelname)s: %(module)s: %(message)s]',
                    
                    handlers=[
                        logging.FileHandler("Logs.log"),
                        logging.StreamHandler(sys.stdout)
                        ]
                    
                    )

FILE_PATHS = [

        Path(f".github/workflows/main.yaml"),
        Path(f"dvc.yaml"),

        Path(f"Artifacts/Info.txt"),

        Path(f"Src/__init__.py"),

        Path(f"Src/Research/experiments.ipynb"),
        
        Path(f"Src/Entities/__init__.py"),
        Path(f"Src/Entities/entity.py"),

        Path(f"Src/Logger.py"),
        Path(f"Src/Exceptions.py"),
        Path(f"Src/Utils.py"),

        Path(f"Src/Config.yaml"),
        Path(f"Src/Params.yaml"),

        Path(f"Src/Configuration/__init__.py"),
        Path(f"Src/Configuration/config.py"),
        
        Path(f"Src/Constant.py"),

        Path(f"Src/Components/__init__.py"),
        Path(f"Src/Pipelines/__init__.py"),
        Path(f"Src/Main.py"),

        Path(f"Application/Info.txt")

]


def create_project_structure(FILE_PATHS):
    
    for file_path in FILE_PATHS:
        

        '''
        Get the Directory and Filename splitted from given 'file_path'
        '''
        directory,filename = os.path.split(file_path)
        


        '''
        Check if the 'directory' is a valid directory or directory path
        
        '''
        if directory!="":
            os.makedirs(directory,exist_ok=True)
            logging.info(f"<<'{directory}'>> Directory Created") 
        else:
            logging.info(f"<<'{directory}'>> is a not Valid directory path or directory")     



        '''
        Check If the 'file_path' exists.
                    OR
        Check If the file at 'file_path' contains some content, 
        if it does then then new file will not be  created.             
        
        '''
        if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        
            with open(file_path,"w") as f:
                logging.info(f"Empty <'{filename}'> in <<'{directory}'>> created!")

        else:

            if os.path.exists(file_path):
                logging.info(f"<'{filename}'> already exists in <<'{directory}'>>")

            if  os.path.getsize(file_path)!=0:
                logging.info(f"<'{filename}'> in <<'{directory}'>> contains some content")   



if __name__ == "__main__":
    
    logging.info("\n====================== Executing template.py  ==========================")
    logging.info("\n==================== Creating project structure ========================\n")
    
    create_project_structure(FILE_PATHS)

    logging.info("\n===================== Project Structure Created! ========================\n")



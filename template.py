import os  #  os is used for generic path generate and acsesss easily
from pathlib import Path
import logging

logging .basicConfig(level=logging.INFO)


project_name = "mlproject"

list_of_files = [
    # ".github/workflows/.gitkeep",#use in deplyment
    f"src/{project_name}/__init__.py",# use __init__ for when it will compile it will make a package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",

    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipelines.py",
    f"src/{project_name}/pipelines/prediction_pipelines.py",

    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"

                 
]

for filepath in list_of_files:
    filepath = Path(filepath)#path open the relative project path
    filedir, filename = os.path.split(filepath) #find directory , path

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
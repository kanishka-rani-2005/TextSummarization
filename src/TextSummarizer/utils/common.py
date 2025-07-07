import os 
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Any, Dict, Union
from box import Box, BoxList,ConfigBox



@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """Reads a yaml file and returns a ConfigBox object.
    Args:
        path_to_yaml (Path): Path to the yaml file.
    Returns:
        ConfigBox: ConfigBox object containing the yaml file data.
    """
    try:
        with open(path_to_yaml, 'r') as stream:
            data = yaml.safe_load(stream)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(data)
    except FileNotFoundError as e:
        logger.error(f"YAML file {path_to_yaml} not found.")
    except Exception as e:
        logger.error(f"Error reading YAML file {path_to_yaml}: {e}")


@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created Directory at : {path}")

        
@ensure_annotations
def get_size(path:Path)->str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"





from src.TextSummarizer.constants import *

from src.TextSummarizer.utils.common import read_yaml, create_directories, get_size
import os
from src.TextSummarizer.logging import logger
import urllib.request as request
from zipfile import ZipFile
from dataclasses import dataclass
from pathlib import Path
from src.TextSummarizer.config.configuration import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config


    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                logger.info(f"Downloading file from: {self.config.source_url}")
                url= self.config.source_url
                file_name = self.config.local_data_file
                file_name , headers =request.urlretrieve(url, file_name)

                logger.info(f"File downloaded: {self.config.local_data_file} of size: {get_size(self.config.local_data_file)}")
            else:
                logger.info(f"File already exists: {self.config.local_data_file} of size: {get_size(self.config.local_data_file)}")


        except Exception as e:
            logger.exception(e)
            raise e
    def extract_zip_file(self):
        try:
            unizip_dir = self.config.unzip_dir
            if not os.path.exists(unizip_dir):
                os.makedirs(unizip_dir)
            logger.info(f"Extracting file: {self.config.local_data_file} to {unizip_dir}")
            with ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unizip_dir)
            logger.info(f"File extracted to: {unizip_dir}")
        except Exception as e:
            logger.exception(e)
            raise e
        
        
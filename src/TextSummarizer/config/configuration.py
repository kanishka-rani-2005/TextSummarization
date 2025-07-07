
from src.TextSummarizer.constants import *
from src.TextSummarizer.utils.common import read_yaml, create_directories
from src.TextSummarizer.entity import DataIngestionConfig
from pathlib import Path


class ConfigManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(Path(config_filepath))
        self.params = read_yaml(Path(params_filepath))
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        data_ingestion_config = self.config.data_ingestion
        create_directories([data_ingestion_config.root_dir])
        return DataIngestionConfig(
            root_dir=Path(data_ingestion_config.root_dir),
            source_url=data_ingestion_config.source_url,
            local_data_file=Path(data_ingestion_config.local_data_file),
            unzip_dir=Path(data_ingestion_config.unzip_dir)
        )
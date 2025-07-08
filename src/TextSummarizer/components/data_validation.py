
from src.TextSummarizer.logging import logger
from src.TextSummarizer.config.configuration import ConfigManager
from src.TextSummarizer.entity import DataValidationConfig
import os

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files(self):
        try:
            logger.info("Validating all files")
        
            validation_status=None
            all_files=os.listdir(os.path.join('artifacts','data_ingestion','samsum_dataset'))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status=False
                    logger.info(f"File {file} is not in the required files list")
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation failed: File {file} is not in the required files list")
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation successful: All required files are present")

            return validation_status
        except Exception as e:
            logger.exception(e)
            raise e

    

from src.TextSummarizer.config.configuration import ConfigManager
from src.TextSummarizer.components.data_validation import DataValidation
from src.TextSummarizer.constants import *

class DataValidationPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            config=ConfigManager()
            data_validation_config=config.get_data_validation()
            data_validation=DataValidation(config=data_validation_config)
            data_validation.validate_all_files()
        except Exception as e:
            print(f"An error occurred: {e}")
            raise e


if __name__ == "__main__":
    try:
        STAGE_NAME = "Data Validation Stage"
        print(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        data_validation_pipeline = DataValidationPipeline()
        data_validation_pipeline.main()
        print(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e


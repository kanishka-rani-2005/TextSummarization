from src.TextSummarizer.components.data_ingestion import DataIngestion
from src.TextSummarizer.config.configuration import ConfigManager
from src.TextSummarizer.logging import logger


class DataIngestionPipeline:
    
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            logger.exception(e)
            raise e



if __name__ == "__main__":
    try:
        STAGE_NAME = "Data Ingestion Stage"
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
    
    
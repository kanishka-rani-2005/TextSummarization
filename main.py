from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.stage1_data_ingestion_pipeline import DataIngestionPipeline

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
    
from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.stage1_data_ingestion_pipeline import DataIngestionPipeline
from src.TextSummarizer.pipeline.stage2_data_validation_pipeline import DataValidationPipeline
from src.TextSummarizer.pipeline.stage3_data_transformation import DataTransformationPipeline
from src.TextSummarizer.pipeline.stage4_model_trainer import ModelTrainerPipeline
from src.TextSummarizer.pipeline.stage5_model_evaluation import ModelEvaluationPipeline

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
    

    try:
        STAGE_NAME = "Data Validation Stage"
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        data_validation_pipeline = DataValidationPipeline()
        data_validation_pipeline.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e

    try:
        STAGE_NAME = "Data Transformation Stage"
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        data_transformation_pipeline = DataTransformationPipeline()
        data_transformation_pipeline.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e
    
    

    try:
        STAGE_NAME = "Model Training Stage"
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        model_trainer_pipeline = ModelTrainerPipeline()
        model_trainer_pipeline.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e
    

    try:
        STAGE_NAME = "Model Evaluation Stage"
        print(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.main()
        print(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e
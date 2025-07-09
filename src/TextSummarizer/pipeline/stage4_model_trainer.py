
from src.TextSummarizer.config.configuration import ConfigManager
from src.TextSummarizer.components.model_trainer import ModelTrainer
from src.TextSummarizer.logging import logger


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config=ConfigManager()
            model_trainer_config=config.get_model_trainer_config()
            model_trainer=ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            logger.error(e)
            raise e



if __name__=='__main__':
    try:
        STAGE_NAME = "Model Training Stage"
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        model_trainer_pipeline = ModelTrainerPipeline()
        model_trainer_pipeline.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e

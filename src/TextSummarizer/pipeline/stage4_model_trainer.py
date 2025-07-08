
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


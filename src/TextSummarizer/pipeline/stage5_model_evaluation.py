from src.TextSummarizer.config.configuration import ConfigManager

from src.TextSummarizer.components.model_evaluation import ModelEvaluation



class ModelEvaluationPipeline:
    def __init__(self):
        pass


    def main(self):
        
        try:
            config = ConfigManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluate()
        except Exception as e:
            raise e
    

if __name__ == "__main__":
    try:
        STAGE_NAME = "Model Evaluation Stage"
        print(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.main()
        print(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e
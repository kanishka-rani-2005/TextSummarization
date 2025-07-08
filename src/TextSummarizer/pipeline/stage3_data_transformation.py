from src.TextSummarizer.config.configuration import ConfigManager
from src.TextSummarizer.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self): 
        try:
            config=ConfigManager()
            data_transformation_config=config.get_data_transformation_config()
            data_transformation=DataTransformation(config=data_transformation_config)
            result=data_transformation.convert_and_save()

        except Exception as e:
            print(f"An error occurred: {e}")
            raise e   


if __name__ == "__main__":
    try:
        STAGE_NAME = "Data Transformation Stage"
        print(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        data_transformation_pipeline = DataTransformationPipeline()
        data_transformation_pipeline.main()
        print(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e



import os 
import urllib.request as request
from zipfile import ZipFile
from src.TextSummarizer.utils.common import get_size
from src.TextSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset , load_from_disk
from src.TextSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
        print(f"Tokenizer name from config: {repr(config.tokenizer_name)}")

    def convert_examples_to_features(self,example_batch):
        input_encodings=self.tokenizer(example_batch['dialogue'],max_length=1024,truncation=True,padding='max_length',return_tensors='pt')

        with self.tokenizer.as_target_tokenizer():
            target_encodings=self.tokenizer(example_batch['summary'],max_length=128,truncation=True,padding='max_length',return_tensors='pt')

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    def convert_and_save(self):
        dataset_samsum=load_from_disk(self.config.data_path)
        dataset_samsum=dataset_samsum.map(self.convert_examples_to_features, batched=True)
        dataset_samsum.save_to_disk(os.path.join(self.config.root_dir,'samsum_dataset'))
        logger.info(f"Saved the dataset to {self.config.root_dir}/samsum_dataset")




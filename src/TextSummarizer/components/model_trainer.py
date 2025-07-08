from transformers import TrainingArguments,Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
from datasets import load_dataset,load_from_disk
import torch
from src.TextSummarizer.config.configuration import ModelTrainerConfig
import os
from src.TextSummarizer.logging import logger


class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config

    def train(self):
        device='cuda' if torch.cuda.is_available() else 'cpu'
        print(device)
        tokenizer=AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus=AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)

        seq2seq_data_collator=DataCollatorForSeq2Seq(tokenizer,model=model_pegasus)

        #loading data
        dataset_samsum_pt=load_from_disk(self.config.data_path)

        logger.info("CPU mode detected. Using a small subset of data for a quick test run.")
        train_dataset_small = dataset_samsum_pt['train'].select(range(200))
        eval_dataset_small = dataset_samsum_pt['validation'].select(range(50))

        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=int(self.config.num_train_epochs), 
            warmup_steps=int(self.config.warmup_steps),
            per_device_eval_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            logging_steps=int(self.config.logging_steps),
            eval_steps=int(self.config.eval_steps),
            save_steps=int(self.config.save_steps),
            gradient_accumulation_steps=int(self.config.gradient_accumulation_steps) 
        )

        trainer=Trainer(
            model=model_pegasus,args=training_args,
            data_collator=seq2seq_data_collator,
            train_dataset=train_dataset_small,
            eval_dataset=eval_dataset_small

        )


        trainer.train()

        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,'pegasus-samsum-model'))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,'tokenizer'))


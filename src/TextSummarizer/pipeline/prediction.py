from src.TextSummarizer.config.configuration import ConfigManager
from transformers import AutoTokenizer, pipeline


class PredictionPipeline:
    def __init__(self):
        self.config=ConfigManager().get_model_evaluation_config() # for model and tokenizer

    def predict(self,text):
        tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs={"length_penalty":0.8 ,'num_beams':8 , 'max_length':128}

        pipe=pipeline('summarization',model=self.config.model_path,tokenizer=tokenizer)


        print('Dialogue')
        print(text)

        output=pipe(text,**gen_kwargs)[0]['summary_text']
        print('\n\nModel Summary')
        print(output)

        return output
    


    



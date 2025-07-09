## Text Summarizer Project


# Overview

This project implements a Text Summarizer using Hugging Face Transformers. It follows a modular pipeline architecture with distinct stages for ingestion, validation, transformation, model training, and evaluation.


## Workflow

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update the components 
6. Update the pipeline
7. Update main.py
8. Update the app.py


## Project Structure

TEXTSUMMARIZATION/
├── artifacts/                  # Stores intermediate pipeline outputs

│   ├── data_ingestion/ 

│   ├── data_transformation/

│   ├── data_validation/

│   ├── model_trainer/

│   └── model_evaluation/

├── config/                    # Configuration files

│   └── config.yaml

├── logs/                      # Logging files

│   └── running_logs.log

├── params/                    # Model & pipeline parameters

│   └── params.yaml

├── research/                  # Experiments and notebooks

├── src/TextSummarizer/       # Source code

│   ├── components/           # Pipeline steps (data loader, trainer, etc.)

│   ├── config/               # Configuration manager

│   ├── constants/            # Project-wide constants

│   ├── entity/               # Data classes for configuration entities

│   ├── logging/              # Logging utility

│   ├── pipeline/             # Pipeline runner scripts

│   ├── utils/                # Utility functions

│   └── __init__.py

├── venv/                      # Virtual environment

├── .gitignore

├── app.log

├── app.py                     # Optional FastAPI app or script

├── Dockerfile                 # For containerizing the application

├── main.py                    # Main entry point

├── README.md

└── requirements.txt



## ⚙️ Setup Instructions
✅ 1. Clone the Repository
``` bash
git clone https://github.com/kanishka-rani-2005/TextSummarization.git
cd TextSummarization
```

✅ 2. Create and Activate Virtual Environment

```bash

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

```
✅ 3. Install Dependencies

```bash
pip install -r requirements.txt
```


##  How to Run the Project
🔹 Step-by-Step Execution
To run the pipeline stages one-by-one, use:

``` bash

python main.py

```


## 🧪 Parameters and Configuration
Update config/config.yaml to change data paths, artifact directories, etc.

Modify params/params.yaml to tweak model-related hyperparameters.


## 🐳 Docker Support (Optional)

🛠️ Build Docker Image

```bash

docker build -t textsummarizer .

```

▶️ Run Container

```bash
docker run -it textsummarizer
```


## 📌 Features
~ Modular architecture

~ Hugging Face Transformer-based summarizer

~ Config-driven pipeline

~ Logging and debugging support

~ Scalable and ready for deployment

## ✍️ Author

Kanishka Rani - kanishka-rani-2005


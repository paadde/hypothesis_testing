from pathlib import Path
import json
import requests
import pandas as pd
from config.settings import DATASET
from config.settings import OWNER
from config.settings import FILE_NAME

# define the config path for the Kaggle API Key
config_path = Path.cwd() / 'config' / 'kaggle.json'

# open and read the Kaggle API Key
with open(config_path) as f:
    kaggle_api = json.load(f)
    username = kaggle_api['username']
    api_key = kaggle_api['key']

# define API url endpoint
base_url = 'https://www.kaggle.com/api/v1'

endpoint_url = (
        f'{base_url}/datasets/download/{OWNER}/{DATASET}/{FILE_NAME}'
        )


response = requests.get(endpoint_url, auth=(username, api_key), stream=True)
response.status_code

# DATA TRANSFORMATION
df = pd.read_csv(response.raw)
df.info()
df.head(10)
df['AgeOfStore'].unique()
df['MarketSize'].unique()
df['LocationID'].unique()

promotion_one_df = df[(df['Promotion'] == 1)]
promotion_one_df.info()
df['AgeOfStore'].unique()

# Create Age Group for each sample
bins = [0, 5, 10, 15, 20, 25, 30]
labels = ['A', 'B', 'C', 'D', 'E', 'F']

df['AgeGroup'] = pd.cut(df['AgeOfStore'], bins=bins, labels=labels)

# Reorder columns
df = df[['MarketID', 'MarketSize', 'LocationID', 'AgeOfStore', 'AgeGroup',
         'Promotion', 'week', 'SalesInThousands']]

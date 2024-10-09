# Import required modules and libraries
from pathlib import Path
import json
import requests
from config.settings import DATASET
from config.settings import OWNER
from config.settings import FILE_NAME


def get_data():
    """
    retrieve data from Kaggle through their public API
    """
    config_path = Path.cwd() / 'config' / 'kaggle.json'

    with open(config_path) as f:
        kaggle_api = json.load(f)
        username = kaggle_api['username']
        api_key = kaggle_api['key']

    base_url = 'https://www.kaggle.com/api/v1'

    endpoint_url = (
        f'{base_url}/datasets/download/{OWNER}/{DATASET}/{FILE_NAME}'
        )

    try:
        response = requests.get(
                endpoint_url,
                auth=(username, api_key),
                stream=True
                )
        print(f'The request returned status_code: {response.status_code}')
    except Exception as e:
        print(f'An error occurred during extraction: {e}')

    return response

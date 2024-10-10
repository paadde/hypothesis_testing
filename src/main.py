import logging
from pathlib import Path
from src.api_client import get_data
from src.data_processing import transform_data
from src.database import upload_to_db


# set up log file to track ETL flow and errors
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[
            logging.FileHandler(Path.cwd() / 'logs' / 'app.log'),
            logging.StreamHandler()
            ]
        )


logger = logging.getLogger(__name__)


def main():
    logger.info('Downloading data from Kaggle...')
    data = get_data()

    logger.info('Transforming data and converting to DataFrame')
    df = transform_data(data)

    # Upload dataframe to the database
    upload_to_db(df, 'marketing_campaign')

    logger.info('ETL Process completed. Script ended.')
    return df


if __name__ == '__main__':
    main()

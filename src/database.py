from pathlib import Path
import pandas as pd
import json
import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import psycopg2


def upload_to_db(df, table_name):
    """
    Upload a dataframe into PostgreSQL Database

    Parameter:
        df = the dataframe to be uploaded
        table_name = name of the table that will be created in the db
    """
    logger = logging.getLogger(__name__)

    # load postgres credential
    logger.info('Loading postgres credentials...')

    try:
        credential = Path.cwd() / 'config' / 'postgres_credential.json'
        with open(credential) as f:
            postgres_auth = json.load(f)
            db_user = postgres_auth['DB_USER']
            db_password = postgres_auth['DB_PASSWORD']
            db_host = postgres_auth['DB_HOST']
            db_name = postgres_auth['DB_NAME']
        logger.info('PostgreSQL credentials loaded.')
    except Exception as e:
        logger.info(f'An error occurred: {e}')

    # set postgres database url
    db_url = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'

    # Creation of SQL Engine
    engine = create_engine(db_url)

    # upload dataframe to postgresql
    try:
        df.to_sql(
                table_name,
                engine,
                if_exists='replace',
                index=False,
                chunksize=1000
                )
        logger.info(
                f'Dataframe was successfully uploaded with name: {table_name}'
                )
        return True
    except SQLAlchemyError as e:
        print(f'An error occurred: {e}')
        return False
    finally:
        engine.dispose()

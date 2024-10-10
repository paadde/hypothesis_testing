import pandas as pd
import logging


def transform_data(data):
    """
    Transform extracted data to a dataframe and create new column for the
    age group
    """
    logger = logging.getLogger(__name__)

    logger.info('Transforming data.raw to a dataframe')

    try:
        df = pd.read_csv(data.raw)
        logger.info('Dataframe conversion succeeded.')
    except Exception as e:
        logger.info(f'failed to transform data: {e}')

    # Create Age Group for each sample
    bins = [0, 5, 10, 15, 20, 25, 30]
    labels = ['A', 'B', 'C', 'D', 'E', 'F']

    # Create new AgeGroup column
    df['AgeGroup'] = pd.cut(df['AgeOfStore'], bins=bins, labels=labels)

    # Reorder columns
    df = df[['MarketID', 'MarketSize', 'LocationID', 'AgeOfStore', 'AgeGroup',
             'Promotion', 'week', 'SalesInThousands']]

    return df

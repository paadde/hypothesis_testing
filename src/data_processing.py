import pandas as pd


def transform_data(data):
    df = pd.read_csv(data.raw)
    return df

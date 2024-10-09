import logging
from src.api_client import get_data
from src.data_processing import transform_data


def main():
    data = get_data()
    df = transform_data(data)
    return df


if __name__ == '__main__':
    main()

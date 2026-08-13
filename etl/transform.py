from etl.extract import extract_market_data
import pandas as pd
from operator import itemgetter

def transform_market_data(extracted_data: list):
    #tasks required(relevant) columns
    columns = ["symbol", "weightedAvgPrice", "openPrice", "highPrice", "lowPrice", "lastPrice", "volume", "quoteVolume", "priceChange"]

    #An itemgetter function to provide a factory to obtain the required columns from each pair data.
    required_columns = itemgetter(*columns)
    cleaned_data = [list(required_columns(pair)) for pair in extracted_data]

    #creating a dataframe with the transformed data
    # print(cleaned_data)
    df = pd.DataFrame(cleaned_data, columns=columns)
    return df
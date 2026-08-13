from etl.extract import extract_market_data
from etl.transform import transform_market_data
from etl.load import load_market_data

if __name__ == "__main__":
    extracted_data = extract_market_data()
    transformed_data = transform_market_data(extracted_data)
    load_market_data(transformed_data)
    print("data upload done!")
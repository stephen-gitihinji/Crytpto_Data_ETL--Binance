import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

def load_market_data(transformed_data: pd.DataFrame):
    conn_str = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    #connecting to the database
    db_connection = create_engine(conn_str)

    #sending the transformed data to the db
    transformed_data.to_sql("crypto_market_data", con=db_connection, if_exists='replace', index=False)
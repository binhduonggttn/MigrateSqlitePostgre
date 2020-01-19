import pandas as pd
import psycopg2
from sqlalchemy import create_engine

df = pd.read_csv('file.csv', sep=';', low_memory=False)
engine = create_engine('postgresql://postgres:1234@127.0.0.1:53807/postgres')
df.to_sql('new_table', con=engine, if_exists='append', index=False, chunksize=20000)
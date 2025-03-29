import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
NETLOC = os.getenv('NETLOC')
PORT = os.getenv('PORT')
DBNAME = os.getenv('DBNAME')

conn_string = f'postgresql://{USER}:{PASSWORD}@{NETLOC}:{PORT}/{DBNAME}'
db = create_engine(conn_string)
conn = db.connect()

file_names = ['name']

for name in file_names:
    df = pd.read_csv(f'./csv_files/{name}.csv')
    df.to_sql(name, con = conn, if_exists='replace', index=False)
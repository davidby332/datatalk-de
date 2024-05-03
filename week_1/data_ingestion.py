import argparse
import os

import pandas as pd

from sqlalchemy import create_engine

def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db_name = params.database_name
    table_name = params.table_name
    data_location = params.data_location
    data_url = params.data_url

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

    print(engine)
    print(data_url)
    print(data_location)

    os.system(f'wget {data_url} -O {data_location}')

    taxi_df = pd.read_parquet(data_location)

    taxi_df.head(0).to_sql(con=engine, name= table_name, if_exists='replace')

    taxi_df.to_sql(con=engine, name= table_name, if_exists='append', chunksize = 25000)


if __name__=='__main__':
    
    parser = argparse.ArgumentParser(description='Ingest NY Taxi Data to Postgres')
    parser.add_argument('--user', help = 'Username for Postgres')
    parser.add_argument('--password', help = 'Password for Postgres')
    parser.add_argument('--host', help = 'Postgres host')
    parser.add_argument('--port', help = 'Port for Postgres')
    parser.add_argument('--database-name')
    parser.add_argument('--table-name')
    parser.add_argument('--data-location')
    parser.add_argument('--data-url')

    args = parser.parse_args()
    
    main(args)

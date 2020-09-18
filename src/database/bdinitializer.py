#!/usr/bin/env python
import os
import pathlib as pl
from playhouse.postgres_ext import *
from dotenv import load_dotenv

env_path = pl.Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

psql_db = PostgresqlExtDatabase(DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

class UserInfo(Model):
    user_id = IntegerField(primary_key=True)
    favourite_films = ArrayField(IntegerField)

    class Meta:
        database = psql_db
    
if __name__ == '__main__':
    psql_db.connect()
    psql_db.create_tables([UserInfo])

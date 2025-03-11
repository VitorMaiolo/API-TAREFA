import os

import psycopg2
from click import password_option
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    conexao = psycopg2.connect(
        dbname=os.getenv(''),
        user=os.getenv(''),
        password=os.getenv(''),
        host=os.getenv(''),
        port=os.getenv('')
    )

    return conexao

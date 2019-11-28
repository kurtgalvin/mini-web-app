import configparser
import psycopg2


def get_db_connection():
    config = configparser.ConfigParser()
    config.read('app/env/config.ini')
    return psycopg2.connect(
        host=config['aws']['host'],
        database=config['aws']['database'],
        user=config['aws']['user'],
        password=config['aws']['password']
    )


class Model:
    def __init__(self):
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM employee;")
                print(cur.fetchmany())
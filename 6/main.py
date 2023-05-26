import os
from db_handler import DbHandler
from tabulate import tabulate

PASSWORD = os.getenv('PASSWORD')
DBNAME = os.getenv('DBNAME')
DSN = f'postgresql://postgres:{PASSWORD}@localhost:5432/{DBNAME}'

if __name__ == '__main__':
    with DbHandler(DSN) as db:
        db.load_fixtures('tests_data.json')
        search = db.find_sales(publisher_id='1')
        headers = ('Book name', 'Publisher', 'Price', 'Date')
        print(tabulate(search, headers, 'presto', numalign='left'))

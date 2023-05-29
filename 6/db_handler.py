from sqlalchemy.orm import sessionmaker
from models import *
import json
from tabulate import tabulate


class DbHandler:
    def __init__(self, DSN):
        self.__engine = sq.create_engine(DSN)
        self.__create_tables(self.__engine)
        self.__Session = sessionmaker(bind=self.__engine)
        self.__s = None

    def __enter__(self):
        self.__s = self.__Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__s:
            self.__s.close()

    @staticmethod
    def __create_tables(engine) -> None:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def load_fixtures(self, path: str) -> None:
        with open(path, 'r') as fd:
            data = json.load(fd)

        for record in data:
            model = {
                'publisher': Publisher,
                'shop': Shop,
                'book': Book,
                'stock': Stock,
                'sale': Sale,
            }[record.get('model')]
            self.__s.add(
                model(id=record.get('pk'), **record.get('fields')))
        self.__s.commit()

    def find_sales(self, id_or_name: int or str) -> None:
        select_all = self.__s.query(Book.title, Shop.name, Sale.price,
                                    Sale.date_sale).join(Publisher).join(
            Stock).join(Shop).join(Sale)

        if type(id_or_name) is int:
            search = select_all.filter(
                Publisher.id == id_or_name).all()
        elif type(id_or_name) is str:
            search = select_all.filter(
                Publisher.name == id_or_name).all()
        else:
            raise TypeError("Please provide string or integer")

        headers = ('Book name', 'Publisher', 'Price', 'Date')
        print(tabulate(search, headers, 'presto', numalign='left'))

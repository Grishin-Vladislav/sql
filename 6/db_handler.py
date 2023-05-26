from sqlalchemy.orm import sessionmaker
from models import *
import json


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

    def find_sales(self, publisher_id: str = None,
                   publisher_name: str = None) -> list:
        if publisher_id:
            return self.__s.query(Book.title, Shop.name, Sale.price,
                                  Sale.date_sale).join(Publisher).join(
                Stock).join(Shop).join(Sale).filter(
                Publisher.id == publisher_id).all()

        if publisher_name:
            return self.__s.query(Book.title, Shop.name, Sale.price,
                                  Sale.date_sale).join(Publisher).join(
                Stock).join(Shop).join(Sale).filter(
                Publisher.name == publisher_name).all()

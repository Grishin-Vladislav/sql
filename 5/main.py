import os
from clients import ClientsHandler

password = os.getenv('PASSWORD')

if __name__ == '__main__':
    with ClientsHandler('clients', password) as db:
        db.drop_all_tables()  # <-- comment this for the first run
        db.create_tables()

        # adding clients and phones
        db.add_client('Вова', 'Кривозуб', 'ggg@gmail.com', '112')
        db.add_client('Маша', 'Иванова', 'tuple@gmail.com', '333')
        db.add_client('Рома', 'Павлов', 'email@ya.ru', '11111')
        db.add_phone(client_id='1', phone='33322211')
        db.add_phone(client_id='2', phone='8800444')
        db.add_phone(client_id='3', phone='22222')
        print(db, '\n')

        # updating info and telephones
        db.update_client_info('1', first_name='Алёша', email='alex@ya.ru')
        db.update_phone(phone_id='1', phone='77788')
        print(db, '\n')

        # deleting phones and clients (deleting client deletes all his phones)
        db.del_phone(phone_id='2')
        db.del_client(client_id='1')
        print(db, '\n')

        # each line below will get the same result - full info about 'Рома' with all phones.
        db.find_client(phone='11111')
        print()
        db.find_client(phone='22222')
        print()
        db.find_client(first_name='Рома')
        print()
        db.find_client(first_name='Рома', phone='11111')

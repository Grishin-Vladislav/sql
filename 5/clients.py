import psycopg2
from tabulate import tabulate


class ClientsHandler:
    """
    Simplifies usage of psycopg2-binary but bind to specific db structure
    which includes 'clients' and 'phone' tables
    before using you may want to create fresh db.
    """

    def __init__(self, database: str, password: str,
                 user: str = 'postgres',
                 host: str = 'localhost',
                 port: str = '5432'):
        self.__database = database
        self.__password = password
        self.__user = user
        self.__host = host
        self.__port = port
        self.__conn = None
        self.__cursor = None

    def __enter__(self):
        self.__conn = psycopg2.connect(database=self.__database,
                                       user=self.__user,
                                       password=self.__password,
                                       host=self.__host,
                                       port=self.__port)

        self.__cursor = self.__conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__cursor:
            self.__cursor.close()

        if self.__conn:
            self.__conn.close()

    def __str__(self):
        raw_table = self.__select_all()
        headers = ('id', 'name', 'last_name', 'email', 'phone', 'phone_id')
        return tabulate(raw_table, headers, 'presto', numalign='left')

    def __select_all(self):
        self.__cursor.execute("""
                    select c.client_id, first_name, 
                            last_name, email, phone_number, phone_id
                    from phone p
                    full join client c on p.client_id = c.client_id
                    order by c.client_id;
                    """)

        return self.__cursor.fetchall()

    def drop_all_tables(self):
        self.__cursor.execute("""
                    drop table phone;
                    drop table client;
                    """)

        self.__conn.commit()

    def create_tables(self):
        self.__cursor.execute("""
                    create table client (
                        client_id serial primary key,
                        first_name varchar(30) not null,
                        last_name varchar(30) not null,
                        email varchar(60) not null unique
                    );
                    """)

        self.__cursor.execute("""
                    create table phone (
                        phone_id serial primary key,
                        client_id integer references client (client_id) 
                                    on delete cascade,
                        phone_number integer not null unique
                    );
                    """)

        self.__conn.commit()

    def add_client(self, first_name: str, last_name: str, email: str,
                   phone: str = None):
        self.__cursor.execute("""
                    insert into client (first_name, last_name, email)
                    values (%s, %s, %s) returning client_id;
                    """, (first_name, last_name, email))

        client_id = self.__cursor.fetchone()[0]
        self.__conn.commit()

        if phone:
            self.__cursor.execute("""
                        insert into phone (client_id, phone_number)
                        values (%s, %s);
                        """, (client_id, phone))

            self.__conn.commit()

    def update_client_info(self, client_id: str,
                           first_name: str = None,
                           last_name: str = None,
                           email: str = None):
        query = 'update client set '
        fields = []

        if first_name:
            query += 'first_name = %s, '
            fields.append(first_name)

        if last_name:
            query += 'last_name = %s, '
            fields.append(last_name)

        if email:
            query += 'email = %s, '
            fields.append(email)

        fields.append(client_id)
        query = query.rstrip(', ')
        query += 'where client_id = %s;'

        self.__cursor.execute(query, tuple(fields))
        self.__conn.commit()

    def del_client(self, client_id: str):
        self.__cursor.execute("""
                    delete from client
                    where client_id = %s;
                    """, client_id)

        self.__conn.commit()

    def add_phone(self, client_id: str, phone: str):
        self.__cursor.execute("""
                    insert into phone (client_id, phone_number)
                    values (%s, %s);
                    """, (client_id, phone))

        self.__conn.commit()

    def update_phone(self, phone_id: str, phone: str):
        self.__cursor.execute("""
                    update phone
                    set phone_number = %s
                    where phone_id = %s;
                    """, (phone, phone_id))

        self.__conn.commit()

    def del_phone(self, phone_id: str):
        self.__cursor.execute("""
                    delete from phone
                    where phone_id = %s
                    """, phone_id)

        self.__conn.commit()

    def find_client(self, first_name: str = None, last_name: str = None,
                    email: str = None, phone: str = None):
        fields = []
        query = """
                select c.client_id, first_name, last_name,
                        email, phone_number, phone_id
                from client c
                join phone p ON p.client_id = c.client_id
                where
                """

        if phone:
            query += """
                     c.client_id in (
                                select client_id
                                from phone
                                where phone_number = %s
                                ) and """
            fields.append(phone)

        if first_name:
            query += 'first_name = %s and '
            fields.append(first_name)

        if last_name:
            query += 'last_name = %s and '
            fields.append(last_name)

        if email:
            query += 'email = %s and '
            fields.append(email)

        query = query.rstrip('and ')

        self.__cursor.execute(query, tuple(fields))
        self.__conn.commit()

        table = self.__cursor.fetchall()
        headers = ('id', 'name', 'last_name', 'email', 'phone', 'phone_id')

        print(tabulate(table, headers, 'presto', numalign='left'))

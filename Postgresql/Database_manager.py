import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class DatabaseManager:
    def __init__(self, user, password, host='localhost', port=5432, dbname=None):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dbname = dbname
        self.connection = None

        if self.dbname:
            self.connect_to_database(self.dbname)

    def create_database(self, dbname):
        conn = psycopg2.connect(
            dbname="postgres",
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (dbname,))
        exists = cur.fetchone()

        if not exists:
            cur.execute(f"CREATE DATABASE {dbname};")
            print(f"Database '{dbname}' created successfully.")
        else:
            print(f"Database '{dbname}' already exists.")
        cur.close()
        conn.close()

    def list_databases(self):
        conn = psycopg2.connect(
            dbname='postgres',
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        cur = conn.cursor()
        cur.execute("SELECT datname FROM pg_database;")
        databases = cur.fetchall()

        print("Available Databases:")
        for db in databases:
            print(f" - {db[0]}")

        cur.close()
        conn.close()

    def connect_to_database(self, dbname):
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.dbname = dbname
        print(f"Connected to database '{dbname}' successfully.")

    def create_table(self, table_name, columns: dict):
        if not self.connection:
            raise Exception("No database connected.")

        cur = self.connection.cursor()

        columns_with_types = []
        for col, dtype in columns.items():
            columns_with_types.append(f"{col} {dtype}")

        columns_with_types = ", ".join(columns_with_types)

        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types});"

        cur.execute(query)
        self.connection.commit()
        print(f"Table '{table_name}' created successfully in '{self.dbname}'.")
        cur.close()

    def insert_data(self, table_name, data: dict):
        if not self.connection:
            raise Exception("No database connected.")

        cur = self.connection.cursor()

        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())

        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"

        cur.execute(query, values)
        self.connection.commit()
        print(f"Data inserted into '{table_name}' successfully.")

        cur.close()

    def show_tables(self):
        if not self.connection:
            raise Exception("No database connected.")

        cur = self.connection.cursor()
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
        tables = cur.fetchall()

        print("Tables in the database:")
        for table in tables:
            print(f" - {table[0]}")

        cur.close()

    def drop_table(self, table_name):
        if not self.connection:
            raise Exception("No database connected.")

        cur = self.connection.cursor()
        cur.execute(f"DROP table {table_name};")
        self.connection.commit()
        print(f"{table_name}' deleted successfully.")
        cur.close()


    def describe_table(self, table_name):
        if not self.connection:
            raise Exception("No database connected.")

        cur = self.connection.cursor()
        cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = %s;", (table_name,))
        columns = cur.fetchall()

        print(f"Description of table '{table_name}':")
        for col in columns:
            print(f" - {col[0]}: {col[1]}")

        cur.close()

    def delete_data(self, table_name, condition):
        if not self.connection:
            raise Exception("No database connected.")

        cur = self.connection.cursor()
        query = f"DELETE FROM {table_name} WHERE {condition};"
        cur.execute(query)
        self.connection.commit()
        print(f"Data deleted from '{table_name}' where {condition}.")

        cur.close()

    def show_data(self, table_name):
        if not self.connection:
            raise Exception("No database connected.")

        cur = self.connection.cursor()
        query = f"SELECT * FROM {table_name};"
        cur.execute(query)
        rows = cur.fetchall()

        print(f"Data from table '{table_name}':")
        for row in rows:
            print(row)

        cur.close()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print(f"Connection to database '{self.dbname}' closed.")
            self.connection = None

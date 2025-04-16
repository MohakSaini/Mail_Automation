import psycopg2

class Database:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.connection = psycopg2.connect(
            database=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            supplier_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20),
            email VARCHAR(100),
            address TEXT
        );
        """)
        self.connection.commit()

    def insert_supplier(self, name, phone, email, address):
        self.cursor.execute("""
            INSERT INTO suppliers (name, phone, email, address)
            VALUES (%s, %s, %s, %s);
        """, (name, phone, email, address))
        self.connection.commit()


    def fetch_suppliers(self):
        self.cursor.execute("SELECT * FROM suppliers;")
        return self.cursor.fetchall()
    
    def delete_supplier_by_id(self, supplier_id):
        self.cursor.execute("DELETE FROM suppliers WHERE supplier_id = %s;", (supplier_id,))
        self.connection.commit()
        print(f"Supplier with ID {supplier_id} has been deleted.")


    def close(self):
        self.connection.close()


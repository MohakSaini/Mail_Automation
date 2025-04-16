import psycopg2

conn = psycopg2.connect(database = "suppliers", 
                        user = "mohak_dev", 
                        host= 'localhost',
                        password = "password",
                        port = 5432)

# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create datacamp_courses table
cur.execute("""select datname from pg_database;""")
# cur.execute("""INSERT INTO suppliers VALUES(1, 'Dotsqaure', '9829388219', 'dots@dots.com', 'jagatpura');""")
# cur.execute("""INSERT INTO suppliers VALUES(2, 'Cynbit', '9834238219', 'cyn@dots.com', 'Pratap nagar');""")
# cur.execute("""INSERT INTO suppliers VALUES(3, 'sqaure', '9829381234', 'square@dots.com', 'Delhi');""")
# cur.execute("""INSERT INTO suppliers VALUES(4, 'Dots', '9829364789', 'dots@dots.com', 'Sitapura');""")
# cur.execute("""select * from suppliers;""")

# Make the changes to the database persistent
rows = cur.fetchall()
for row in rows:
    print(row)


conn.commit()
conn.close()



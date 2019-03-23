import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=root port=5432")

c = conn.cursor()
def create_table():

    c.execute('CREATE TABLE users(id integer PRIMARY KEY,email text,name text,address text)')
    conn.commit()

    insert_query = "INSERT INTO users VALUES {}".format("(10, 'hello@dataquest.io', 'Some Name', '123 Fake St.')")
    c.execute(insert_query)
    conn.commit()

    c.execute('SELECT * FROM users')




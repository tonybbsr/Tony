import psycopg2
from Config import config
import csv

#Hi Tony

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # execute a statement
        # print('PostgreSQL database table Creation')
        # cur.execute('CREATE TABLE users1(id integer PRIMARY KEY,email text,name text,address text)')
        # conn.commit()

        # insert a statement
        print('PostgreSQL data insertion')
        cur.execute("INSERT INTO users VALUES {}".format("(14, 'hello@dataquest.io', 'Some Name', '123 Fake St.')"))
        conn.commit()
        # insert_query = "INSERT INTO users VALUES {}".format("(10, 'hello@dataquest.io', 'Some Name', '123 Fake St.')")
        # cur.execute(insert_query)
        # conn.commit()

        #Load Data From Csv
        with open('user_accounts.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row.
            for row in reader:
                cur.execute(
                    "INSERT INTO users VALUES (%s, %s, %s, %s)",
                    row
                )
        conn.commit()


        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
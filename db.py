import sys
import os
import psycopg2

database = sys.argv[1]
user = os.environ.get('PGUSER')
passw = os.environ.get('PGPASSWORD')
host = os.environ.get('PGHOST')
port = os.environ.get('PGPORT')

f = open("number.txt")
number = f.read()

Lx = 2000+5*int(number)
conn = psycopg2.connect(database = database, user = user, password = passw, host=host, port=port)
query = "select ISBN_no from book_catalogue where year = " + str(Lx)
try:
    cur = conn.cursor()
    cur.execute(query)

    result = cur.fetchall()
    
    for r in result:
        print(r[0])
except:
    print("exceptiom")
finally:
    cur.close()
    conn.close()
    
    1000011
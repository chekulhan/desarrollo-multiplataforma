# No te olvides crear un entorno virtual, y ejecutar 'pip install psycopg2-binary'

import psycopg2

# connection
# host = he mapeado el puerto 5432 en el docker compose file, para que este disponible
conn = psycopg2.connect(
    dbname="odoo",
    user="odoo",
    password="odoo",
    host="localhost",   # "localhost" or "db" if inside Docker 
    port="5432"
)

# cursor
cur = conn.cursor()

# query
cur.execute("SELECT version();")

# result
print(cur.fetchone())

# Query the Odoo contacts table (res_partner)
cur.execute("SELECT id, name, email FROM res_partner LIMIT 10;")
rows = cur.fetchall()

for row in rows:
    print(row)

# cleanup
cur.close()

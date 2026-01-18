import psycopg2

connection = psycopg2.connect(
    host="34.47.233.110",
    port=5432,
    database="empdb",
    user="cloud-postgres2",
    password="Shashi@2004",
    sslmode="require"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM employee;")
data = cursor.fetchall()

for row in data:
    print(row)

cursor.close()
connection.close()

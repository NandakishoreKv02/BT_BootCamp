import psycopg2

connection = psycopg2.connect(
    host="database-1.cr80qkccc210.ap-south-1.rds.amazonaws.com",
    port=5432,
    database="bt_intern_db",
    user="postgres",
    password="9740138976"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM employees;")
data = cursor.fetchall()

for row in data:
    print(row)

cursor.close()
connection.close()



# sql = """
#     INSERT INTO employees
#     VALUES (%s, %s, %s, %s)
# """
# params = (4,'Shashi', 'Corporate', 'Hirehalli')

# cursor.execute(sql,params)
# connection.commit()

# cursor.close()
# connection.close()
import mariadb

conn = mariadb.connect(
    user="employees",
    password="employees",
    host="localhost",
    port=3306,
    database="employees"
)

cur = conn.cursor()

cur.execute("select id, emp_name from employees")

for (id, name) in cur:
    print(id, name)

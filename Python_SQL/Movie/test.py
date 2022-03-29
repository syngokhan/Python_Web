import psycopg2

url = "postgres://aapifbiz:qgSECeWTmHD8sf_K90Rem_hgMLQLPr3s@kandula.db.elephantsql.com/aapifbiz"
connection = psycopg2.connect(url)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")
first_user = cursor.fetchone()

print(first_user)

connection.close()
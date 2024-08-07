import pyodbc

# Configura los parámetros de conexión
server = 'localhost'
database = 'PRACTICA1'  # Nombre de la base de datos
username = 'root'
password = '3191363100501'

# Establece la conexión
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'UID=' + username + ';'
    'PWD=' + password + ';'
    'TrustServerCertificate=yes;'
)

# Crea un cursor
cursor = conn.cursor()

# Ejecuta una consulta
# cursor.execute("SELECT * FROM avion;")
cursor.execute("SELECT @@VERSION;")

# Obtiene el resultado
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()

# Cierra la conexión
conn.close()

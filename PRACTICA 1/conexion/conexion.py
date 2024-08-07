import pyodbc
from conexion.config import DATABASE_CONFIG

def get_connection():
    conn_str = (
        'DRIVER=ODBC Driver 17 for SQL Server;'
        'SERVER=localhost;'
        'DATABASE=PRACTICA1;'
        'UID=root;'
        'PWD=3191363100501'
    ).format(**DATABASE_CONFIG)
    return pyodbc.connect(conn_str)
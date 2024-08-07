from conexion.conexion import get_connection

def modelo_borrar():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("DROP TABLE IF EXISTS PASSENGER_AIRPORT")
    cursor.execute("DROP TABLE IF EXISTS FLIGHTS")
    cursor.execute("DROP TABLE IF EXISTS PASSENGERS")
    cursor.execute("DROP TABLE IF EXISTS AIRPORTS")
    conexion.commit()
    cursor.close()
    conexion.close()

    print("-------- MODELO ELIMINADO CON EXITO --------")

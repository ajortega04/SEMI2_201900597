import pandas as pd

def transformar_info(datos):
    # Conversión de la columna 'DepartureDate' al tipo de dato de fecha
    datos['DepartureDate'] = pd.to_datetime(datos['Departure Date'], errors='coerce')
    
    # Conversión de 'Gender' a tipo BIT (0 para Male, 1 para Female)
    datos['Gender'] = datos['Gender'].apply(lambda x: 1 if x == 'Female' else 0)

    # Eliminar duplicados en 'Passenger ID'
    # datos.drop_duplicates(subset=['Passenger ID'], keep='first', inplace=True)
    # mZWjgO
    
    # Eliminar registros con 'Arrival Airport' nulo o 0
    datos = datos[datos['Arrival Airport'].notnull() & (datos['Arrival Airport'] != "0")]

    return datos
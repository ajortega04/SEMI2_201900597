import pandas as pd
from conexion.conexion import get_connection

def cargar_info(datos):

    # Limpiar datos duplicados y nulos
    # datos = datos = datos.drop_duplicates(subset=['Passenger ID']).copy()
    # datos_b = datos.drop_duplicates(subset=['Airport Name', 'Airport Country Code']).copy()
    # datos = datos[datos['Arrival Airport'].notna() & (datos['Arrival Airport'] != "0")]
    
    cargar_pasajeros(datos) 
    cargar_aeropuerto(datos)
    cargar_vuelos(datos)
    
def cargar_pasajeros(datos):
    conexion = get_connection()
    cursor = conexion.cursor()
    for index, row in datos.iterrows():
        cursor.execute("""
            IF NOT EXISTS (SELECT 1 FROM PASSENGERS WHERE PassengerID = ?)
            BEGIN
                INSERT INTO PASSENGERS (PassengerID, FirstName, LastName, Gender, Age, Nationality)
                VALUES (?, ?, ?, ?, ?, ?)
            END
            """, 
            row['Passenger ID'],
            row['Passenger ID'], row['First Name'], row['Last Name'], row['Gender'], row['Age'], row['Nationality']
        )
    conexion.commit()
    cursor.close()
    conexion.close()

def cargar_aeropuerto(datos):
    conexion = get_connection()
    cursor = conexion.cursor()

    # Eliminar duplicados en el DataFrame, manteniendo solo la primera aparición
    datos = datos.drop_duplicates(subset=['Airport Name', 'Airport Country Code']).copy()
    
    # Obtener los registros existentes de la base de datos
    cursor.execute("SELECT AirportName, AirportCountry FROM AIRPORTS")
    existing_airports = set((row[0], row[1]) for row in cursor.fetchall())

    print("Existing airports in database:")
    for airport in existing_airports:
        print(airport)

    print("\nData to be inserted:")
    for index, row in datos.iterrows():
        airport_key = (row['Airport Name'], row['Airport Country Code'])
        # print(airport_key)  # Para verificar los datos que se están tratando de insertar
        if airport_key not in existing_airports:
            cursor.execute("""
                INSERT INTO AIRPORTS (
                    AirportName, AirportCountry, CountryName, AirportContinent, Continents
                )
                VALUES (?, ?, ?, ?, ?)
                """, 
                row['Airport Name'], row['Airport Country Code'], 
                row['Country Name'], row['Airport Continent'], row['Continents']
            )
            # Agregar el nuevo aeropuerto al conjunto existente
            existing_airports.add(airport_key)
    conexion.commit()
    cursor.close()
    conexion.close()

def cargar_vuelos(datos):
    conexion = get_connection()
    cursor = conexion.cursor()
    for index, row in datos.iterrows():
        cursor.execute("""
            IF NOT EXISTS (SELECT 1 FROM FLIGHTS 
                            WHERE DepartureDate = ? 
                              AND ArrivalAirport = ? 
                              AND PilotName = ? 
                              AND PassengerID = ?)
            BEGIN
                INSERT INTO FLIGHTS (DepartureDate, ArrivalAirport, PilotName, FlightStatus, PassengerID, AirportName)
                VALUES (?, ?, ?, ?, ?, ?)
            END
            """, 
            row['Departure Date'], row['Arrival Airport'], row['Pilot Name'], row['Passenger ID'], 
            row['Departure Date'], row['Arrival Airport'], row['Pilot Name'], row['Flight Status'], row['Passenger ID'], row['Airport Name']
        )
    conexion.commit()
    cursor.close()
    conexion.close()
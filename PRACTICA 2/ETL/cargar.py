import pandas as pd
from conexion.conexion import get_connection

def cargar_info(datos):    
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
                    AirportName, AirportCountry, CountryName, AirportContinent, Continents)
                VALUES (?, ?, ?, ?, ?)
                """, 
                row['Airport Name'], row['Airport Country Code'], row['Country Name'], row['Airport Continent'], row['Continents']
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
        if row['Arrival Airport'] != '0':
            cursor.execute("""
                INSERT INTO FLIGHTS (DepartureDate, ArrivalAirport, PilotName, FlightStatus)
                VALUES (?, ?, ?, ?)
                """, 
                row['Departure Date'], row['Arrival Airport'], row['Pilot Name'], row['Flight Status']
            )

    conexion.commit()
    cursor.close()
    conexion.close()

def cargar_pasajero_aeropuerto(datos):
    conexion = get_connection()
    cursor = conexion.cursor()
    
    for index, row in datos.iterrows():
        # Verificar que el PassengerID existe en la tabla PASSENGERS
        cursor.execute("""
            SELECT COUNT(*)
            FROM PASSENGERS
            WHERE PassengerID = ?
            """, row['Passenger ID'])
        passenger_exists = cursor.fetchone()[0]
        
        # Obtener el AirportID basado en AirportName y AirportCountry
        cursor.execute("""
            SELECT AirportID
            FROM AIRPORTS
            WHERE AirportName = ? AND AirportCountry = ?
            """, row['Airport Name'], row['Airport Country Code'])
        airport_id = cursor.fetchone()
        
        # Obtener el FlightID basado en los detalles del vuelo
        cursor.execute("""
            SELECT FlightID
            FROM FLIGHTS
            WHERE DepartureDate = ? AND ArrivalAirport = ? AND PilotName = ? AND FlightStatus = ?
            """, 
            row['Departure Date'], row['Arrival Airport'], row['Pilot Name'], row['Flight Status'])
        flight_id = cursor.fetchone()
        
        # Si se encuentran el pasajero y el vuelo, y se ha encontrado un AirportID correspondiente
        if passenger_exists and airport_id is not None and flight_id is not None:
            airport_id = airport_id[0]  # Obtener el AirportID del resultado de la consulta
            flight_id = flight_id[0]    # Obtener el FlightID del resultado de la consulta
            
            # Insertar en la tabla FACT_FLIGHT_DETAILS si no existe
            cursor.execute("""
                INSERT INTO FACT_FLIGHT_DETAILS (PassengerID, AirportID, FlightID)
                VALUES (?, ?, ?)
                """, 
                row['Passenger ID'], airport_id, flight_id
            )
    
    conexion.commit()
    cursor.close()
    conexion.close()

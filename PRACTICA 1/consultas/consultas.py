import pyodbc

def get_connection():
    conn_str = (
        'DRIVER=ODBC Driver 17 for SQL Server;'
        'SERVER=localhost;'
        'DATABASE=PRACTICA1;'
        'UID=root;'
        'PWD=3191363100501'
    )
    return pyodbc.connect(conn_str)


def execute_query(query):
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conexion.close()
    return results

# 1. Contar el número de registros en cada tabla
def count_records():
    queries = [
        "SELECT 'PASSENGERS' AS TableName, COUNT(*) AS RecordCount FROM PASSENGERS",
        "SELECT 'AIRPORTS', COUNT(*) FROM AIRPORTS",
        "SELECT 'FLIGHTS', COUNT(*) FROM FLIGHTS",
        "SELECT 'FACT_FLIGHT_DETAILS', COUNT(*) FROM FACT_FLIGHT_DETAILS"
    ]
    for query in queries:
        results = execute_query(query)
        print(results)

# 2. Porcentaje de pasajeros por género
def percentage_by_gender():
    query = """
    SELECT 
        CASE 
            WHEN Gender = '0' THEN 'Hombre'
            WHEN Gender = '1' THEN 'Mujer'
        END AS GenderDescription,
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM PASSENGERS) AS Percentage
    FROM PASSENGERS
    GROUP BY Gender
    """
    results = execute_query(query)
    print(results)

# 3. Nacionalidades con su mes y año de mayor fecha de salida (asumiendo que DepartureDate está en FACT_FLIGHT_DETAILS)
def nationalities_by_month_year():
    query = """
    SELECT 
        p.Nationality,
        FORMAT(f.DepartureDate, 'MM-yyyy') AS MonthYear,
        COUNT(*) AS FlightCount
    FROM FACT_FLIGHT_DETAILS fd
    JOIN PASSENGERS p ON fd.PassengerID = p.PassengerID
    JOIN FLIGHTS f ON fd.FlightID = f.FlightID
    GROUP BY p.Nationality, FORMAT(f.DepartureDate, 'MM-yyyy')
    ORDER BY 
        p.Nationality, 
        MIN(f.DepartureDate);
    """
    results = execute_query(query)
    for row in results:
        print(f"Nacionalidad: {row.Nationality}, Fecha: {row.MonthYear}, Pasajeros: {row.FlightCount}")
    # print(results)

# 4. Conteo de vuelos por país
def passengers_by_country():
    query = """
    SELECT 
        a.AirportCountry AS Country,
        COUNT(DISTINCT fd.PassengerID) AS PassengerCount
    FROM FACT_FLIGHT_DETAILS fd
    JOIN AIRPORTS a ON fd.AirportID = a.AirportID
    GROUP BY a.AirportCountry
    ORDER BY PassengerCount DESC;
    """
    results = execute_query(query)
    
    print("Count de Pasajeros por País:")
    for row in results:
        print(f"País: {row.Country}, Pasajeros: {row.PassengerCount}")

# 5. Top 5 aeropuertos con mayor número de pasajeros
def top_5_airports():
    query = """
    SELECT 
        a.AirportName,
        COUNT(f.PassengerID) AS PassengerCount
    FROM FACT_FLIGHT_DETAILS f
    JOIN AIRPORTS a ON f.AirportID = a.AirportID
    GROUP BY a.AirportName
    ORDER BY PassengerCount DESC
    OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY
    """
    results = execute_query(query)
    print(results)

# 6. Conteo dividido por estado de vuelo
def flights_by_status():
    query = """
    SELECT 
        FlightStatus,
        COUNT(*) AS FlightCount
    FROM FLIGHTS
    GROUP BY FlightStatus
    """
    results = execute_query(query)
    print(results)

# 7. Top 5 países más visitados
def top_5_countries():
    query = """
    SELECT 
        a.AirportCountry,
        COUNT(f.FlightID) AS FlightCount
    FROM FACT_FLIGHT_DETAILS f
    JOIN AIRPORTS a ON f.AirportID = a.AirportID
    GROUP BY a.AirportCountry
    ORDER BY FlightCount DESC
    OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY
    """
    results = execute_query(query)
    print(results)

# 8. Top 5 continentes más visitados
def top_5_continents():
    query = """
    SELECT TOP 5
        a.Continents AS Continent,
        COUNT(DISTINCT fd.PassengerID) AS PassengerCount
    FROM FACT_FLIGHT_DETAILS fd
    JOIN AIRPORTS a ON fd.AirportID = a.AirportID
    GROUP BY a.Continents
    ORDER BY PassengerCount DESC;
    """
    results = execute_query(query)
    
    print("Count de Pasajeros por Continente:")
    for row in results:
        print(f"Continente: {row.Continent}, Pasajeros: {row.PassengerCount}")

# 9. Top 5 edades divididas por género que más viajan
def top_5_ages_by_gender():
    query = """
    WITH AgeGenderCounts AS (
        SELECT 
            p.Gender,
            p.Age,
            COUNT(fd.PassengerID) AS PassengerCount
        FROM PASSENGERS p
        JOIN FACT_FLIGHT_DETAILS fd ON p.PassengerID = fd.PassengerID
        GROUP BY p.Gender, p.Age
    )
    SELECT 
        Gender = CASE WHEN Gender = 0 THEN 'Hombre' ELSE 'Mujer' END,
        Age,
        PassengerCount
    FROM (
        SELECT TOP 5
            Gender,
            Age,
            PassengerCount
        FROM AgeGenderCounts
        WHERE Gender = 0
        ORDER BY PassengerCount DESC
    ) AS TopMales
    
    UNION ALL
    
    SELECT 
        Gender = CASE WHEN Gender = 0 THEN 'Hombre' ELSE 'Mujer' END,
        Age,
        PassengerCount
    FROM (
        SELECT TOP 5
            Gender,
            Age,
            PassengerCount
        FROM AgeGenderCounts
        WHERE Gender = 1
        ORDER BY PassengerCount DESC
    ) AS TopFemales;
    """
    results = execute_query(query)
    
    print("Top 5 Edades por Género que Más Viajan:")
    for row in results:
        print(f"Género: {row.Gender}, Edad: {row.Age}, Pasajeros: {row.PassengerCount}")

# 10. Conteo de vuelos por mes y año
def flights_by_month_year():
    query = """
    SELECT 
        FORMAT(DepartureDate, 'MM-yyyy') AS MonthYear,
        COUNT(*) AS FlightCount
    FROM FLIGHTS
    GROUP BY FORMAT(DepartureDate, 'MM-yyyy')
    ORDER BY MonthYear
    """
    results = execute_query(query)
    
    print("Count de vuelos por MM-YYYY")
    for row in results:
        print(f"Mes: {row.MonthYear}, Pasajeros: {row.FlightCount}")
    # print(results)

# Llamar a las funciones para obtener los resultados
# count_records()
# percentage_by_gender()
# nationalities_by_month_year()
# passengers_by_country()
# top_5_airports()
# flights_by_status()
# top_5_countries()
# top_5_continents()
# top_5_ages_by_gender()
# flights_by_month_year()
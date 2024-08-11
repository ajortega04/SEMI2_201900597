from conexion.conexion import get_connection

def modelo_crear():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
CREATE TABLE PASSENGERS (
    PassengerID VARCHAR(50) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender BIT,
    Age INT,
    Nationality VARCHAR(50)
);

CREATE TABLE AIRPORTS (
    AirportID INT IDENTITY(1,1) PRIMARY KEY,
    AirportName VARCHAR(100),
    AirportCountry VARCHAR(50),
    CountryName VARCHAR(50),
    AirportContinent VARCHAR(30),
    Continents VARCHAR(30)
);

CREATE TABLE FLIGHTS (
    FlightID INT PRIMARY KEY IDENTITY(1,1),
    DepartureDate DATE,
    ArrivalAirport VARCHAR(10),
    PilotName VARCHAR(100),
    FlightStatus VARCHAR(20)
);

CREATE TABLE FACT_FLIGHT_DETAILS (
    FactID INT IDENTITY(1,1) PRIMARY KEY,
    PassengerID VARCHAR(50),
    AirportID INT,
    FlightID INT,
    FOREIGN KEY (PassengerID) REFERENCES PASSENGERS(PassengerID),
    FOREIGN KEY (AirportID) REFERENCES AIRPORTS(AirportID),
    FOREIGN KEY (FlightID) REFERENCES FLIGHTS(FlightID)
);

""")
    
    conexion.commit()
    cursor.close()
    conexion.close()

    print("-------- MODELO CREADO CON EXITO --------")
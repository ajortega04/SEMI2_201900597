SELECT * FROM FLIGHTS WHERE ArrivalAirport = '0'

SELECT * FROM AIRPORTS
SELECT * FROM PASSENGERS
SELECT * FROM FACT_FLIGHT_DETAILS

-----------------------------------
DROP TABLE IF EXISTS FACT_FLIGHT_DETAILS
DROP TABLE IF EXISTS FLIGHTS
DROP TABLE IF EXISTS PASSENGERS
DROP TABLE IF EXISTS AIRPORTS

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

-----------------------------
--CONSULTA 1
SELECT 'PASSENGERS' AS TableName, COUNT(*) AS RecordCount FROM PASSENGERS
UNION ALL
SELECT 'AIRPORTS', COUNT(*) FROM AIRPORTS
UNION ALL
SELECT 'FLIGHTS', COUNT(*) FROM FLIGHTS
UNION ALL
SELECT 'FACT_FLIGHT_DETAILS', COUNT(*) FROM FACT_FLIGHT_DETAILS;

-- CONSULTA 2
SELECT 
    CASE 
        WHEN Gender = '0' THEN 'Hombre'
        WHEN Gender = '1' THEN 'Mujer'
    END AS GenderDescription,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM PASSENGERS) AS Percentage
FROM PASSENGERS
GROUP BY Gender

--CONSULTA 3
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

-- CONSULTA 4
SELECT 
    a.AirportCountry AS Country,
    COUNT(DISTINCT fd.PassengerID) AS PassengerCount
FROM FACT_FLIGHT_DETAILS fd
JOIN AIRPORTS a ON fd.AirportID = a.AirportID
GROUP BY a.AirportCountry
ORDER BY PassengerCount DESC;

-- CONSULTA 5
SELECT 
    a.AirportName,
    COUNT(f.PassengerID) AS PassengerCount
FROM FACT_FLIGHT_DETAILS f
JOIN AIRPORTS a ON f.AirportID = a.AirportID
GROUP BY a.AirportName
ORDER BY PassengerCount DESC
OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY

-- CONSULTA 6
SELECT 
    FlightStatus,
    COUNT(*) AS FlightCount
FROM FLIGHTS
GROUP BY FlightStatus

-- CONSULTA 7
SELECT 
    a.AirportCountry,
    COUNT(f.FlightID) AS FlightCount
FROM FACT_FLIGHT_DETAILS f
JOIN AIRPORTS a ON f.AirportID = a.AirportID
GROUP BY a.AirportCountry
ORDER BY FlightCount DESC
OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY

-- CONSULTA 8
SELECT TOP 5
    a.Continents AS Continent,
    COUNT(DISTINCT fd.PassengerID) AS PassengerCount
FROM FACT_FLIGHT_DETAILS fd
JOIN AIRPORTS a ON fd.AirportID = a.AirportID
GROUP BY a.Continents
ORDER BY PassengerCount DESC;

-- CONSULTA 9
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

-- CONSULTA 10
SELECT 
    FORMAT(DepartureDate, 'MM-yyyy') AS MonthYear,
    COUNT(*) AS FlightCount
FROM FLIGHTS
GROUP BY FORMAT(DepartureDate, 'MM-yyyy')
ORDER BY MonthYear
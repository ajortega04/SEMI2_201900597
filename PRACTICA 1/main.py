from ETL.cargar import *
from ETL.extraer import extraer_info
from ETL.transformar import transformar_info
from modelo.modelo_borrar import modelo_borrar
from modelo.modelo_crear import modelo_crear
from conexion.conexion import get_connection
from consultas.consultas import *

def main():
    activo = True
    datos = ""
    while activo:
        print("\n+-----------------------------------+")
        print("|----- PRACTICA 1 - 201900597 ------|")
        print("+-----------------------------------+")
        print("|- 1. BORRAR MODELO       ----------|")
        print("|- 2. CREAR MODELO        ----------|")
        print("|- 3. EXTRAER INFORMACION ----------|")
        print("|- 4. CARGAR INFORMACION  ----------|")
        print("|- 5. REALIZAR CONSULTAS  ----------|")
        print("|- 6. SALIR               ----------|")
        print("+-----------------------------------+\n")

        opcion = input("Ingrese una de las opciones: ")

        if opcion == "1":
            print("|- 1. BORRAR MODELO       ----------|\n")
            modelo_borrar()

        elif opcion == "2":
            print("|- 2. CREAR MODELO        ----------|\n")
            modelo_crear()

        elif opcion == "3":    
            print("|- 3. EXTRAER INFORMACION ----------|\n")
            ruta = input("Ingrese la ruta del archivo: ")
            try:
                datos = extraer_info(ruta)
            except Exception as e:
                print("#### ERROR AL CARGAR EL ARCHIVO ###")

        elif opcion == "4":
            print("|- 4. CARGAR INFORMACION  ----------|\n")
            try:
                data = transformar_info(datos)
                # print(data)
                activo2 = True
                while activo2:
                    print("\n+-----------------------------------+")
                    print("|- 1. CARGAR PASAJEROS    ----------|")
                    print("|- 2. CARGAR AEROPUERTOS  ----------|")
                    print("|- 3. CARGAR VUELO        ----------|")
                    print("|- 4. CARGAR PASAJERO-AEROPUERTO ---|")
                    print("|- 5. SALIR               ----------|")
                    print("+-----------------------------------+\n")
                    opcion2 = input("ingrese la opcion que desea: ")
                    if opcion2 == "1":
                        cargar_pasajeros(data)
                    elif opcion2 == "2":
                        cargar_aeropuerto(data)
                    elif opcion2 == "3":
                        cargar_vuelos(data)
                    elif opcion2 == "4":
                        cargar_pasajero_aeropuerto(data)
                    else:
                        activo2 = False


            except Exception as e:
                print("#### ERROR - AUN NO HAY DATOS EN EL SISTEMA ###")
                print(e)

        elif opcion == "5":
            print("|- 5. REALIZAR CONSULTAS  ----------|\n")
            activo2 = True
            while activo2:
                print("\n+-----------------------------------+")
                print("|- 1. DATOS TABLAS        ----------|")
                print("|- 2. PORCENTAJE GENERO   ----------|")
                print("|- 3. CONSULTA 3          ----------|")
                print("|- 4. CONTADOR VUELOS PAIS ---------|")
                print("|- 5. TOP 5 AEROPUERTOS   ----------|")
                print("|- 6. CONTADOR DIV X ESTADO VUELO --|")
                print("|- 7. TOP 5 PAISES VISITADOS -------|")
                print("|- 8. TOP 5 CONTINENTES VISITADOS --|")
                print("|- 9. TOP 5 EDADES POR GENERO    ---|")
                print("|- 10. CONTADOR DE VUELOS POR MES --|")
                print("|- 11. SALIR              ----------|")
                print("+-----------------------------------+\n")
                opcion2 = input("ingrese la opcion que desea: ")
                if opcion2 == "1":
                    count_records()
                elif opcion2 == "2":
                    percentage_by_gender()
                elif opcion2 == "3":
                    nationalities_by_month_year()
                elif opcion2 == "4":
                    passengers_by_country()
                if opcion2 == "5":
                    top_5_airports()
                elif opcion2 == "6":
                    flights_by_status()
                elif opcion2 == "7":
                    top_5_countries()
                if opcion2 == "8":
                    top_5_continents()
                elif opcion2 == "9":
                    top_5_ages_by_gender()
                elif opcion2 == "10":
                    flights_by_month_year()
                else:
                    activo2 = False

        elif opcion == "6":
            print("|- 6. SALIR               ----------|\n")
            break

        else:
            print("error")
            # extraer_info()
            # transformar_info()
            conexion = get_connection()
            print(conexion)

if __name__ == '__main__':
    main()
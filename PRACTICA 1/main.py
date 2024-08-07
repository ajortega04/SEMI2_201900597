from ETL.cargar import *
from ETL.extraer import extraer_info
from ETL.transformar import transformar_info
from modelo.modelo_borrar import modelo_borrar
from modelo.modelo_crear import modelo_crear
from conexion.conexion import get_connection

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
            # try:
            datos = extraer_info(ruta)
            # except Exception as e:
            #     print("#### ERROR AL CARGAR EL ARCHIVO ###")

        elif opcion == "4":
            print("|- 4. CARGAR INFORMACION  ----------|\n")
            # try:
            data = transformar_info(datos)
            # print(data)
            activo2 = True
            while activo2:
                print("\n+-----------------------------------+")
                print("|- 1. CARGAR PASAJEROS    ----------|")
                print("|- 2. CARGAR AEROPUERTOS  ----------|")
                print("|- 3. CARGAR VUELO        ----------|")
                print("|- 4. SALIR               ----------|")
                print("+-----------------------------------+\n")
                opcion2 = input("ingrese la opcion que desea: ")
                if opcion2 == "1":
                    cargar_pasajeros(data)
                elif opcion2 == "2":
                    cargar_aeropuerto(data)
                elif opcion2 == "3":
                    cargar_vuelos(data)
                else:
                    activo2 = False


            # except Exception as e:
                # print("#### ERROR - AUN NO HAY DATOS EN EL SISTEMA ###")
                # print(e)

        elif opcion == "5":
            print("|- 5. REALIZAR CONSULTAS  ----------|\n")
            cargar_info()

        elif opcion == "6":
            print("|- 6. SALIR               ----------|\n")
            activo = False

        else:
            print("error")
            # extraer_info()
            # transformar_info()
            conexion = get_connection()
            print(conexion)

if __name__ == '__main__':
    main()
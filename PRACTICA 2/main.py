from ETL.cargar import *
from ETL.extraer import extraer_info
from ETL.transformar import transformar_info
from consultas.consultas import *

def main():
    datos = ""
    print("\n+-----------------------------------+")
    print("|----- PRACTICA 2 - 201900597 ------|")
    print("+-----------------------------------+")

    try:
        ruta = input("Ingrese la ruta del archivo: ")
        datos = extraer_info(ruta)
        print(datos)
    except Exception as e:
        print("#### ERROR AL CARGAR EL ARCHIVO ###")

    try:
        datos = transformar_info(datos)
        print(datos)

        promedio_calificaciones(datos)
        curso_min_max(datos)
        horario_flexible(datos)

        graficar_nivel_dificultad(datos)
        graficar_categorias(datos)
        graficar_duracion_revisiones(datos)
        graficar_histograma_duracion(datos)
        graficar_cajas_calificaciones(datos)

        # print(data)
        # cargar_pasajeros(data)

    except Exception as e:
        # print("#### ERROR - AUN NO HAY DATOS EN EL SISTEMA ###")
        print(e)

if __name__ == '__main__':
    main()
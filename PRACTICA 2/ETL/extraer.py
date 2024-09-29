import pandas as pd

def extraer_info(ruta):
    print("Extraer")
    data = pd.read_csv(ruta, delimiter=',')
    print(data.columns)  # Imprimir nombres de columnas para verificación
    return pd.read_csv(ruta, delimiter=',')

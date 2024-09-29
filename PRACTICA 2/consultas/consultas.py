import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def promedio_calificaciones(datos):
    # Calcular el promedio de calificaciones por curso
    promedio = datos.groupby('Course Title')['Rating'].mean().reset_index()
    print("----------------------------------------------------------------")
    print("Promedio de calificaciones por curso:\n", promedio)
    print("----------------------------------------------------------------")
    return promedio  # Devuelve el DataFrame con el promedio

def curso_min_max(datos):
    curso_max = datos.loc[datos['Rating'].idxmax()]
    curso_min = datos.loc[datos['Rating'].idxmin()]
    print("----------------------------------------------------------------")
    print("Curso con mayor rating:\n", curso_max)
    print("----------------------------------------------------------------")
    print("Curso con menor rating:\n", curso_min)
    print("----------------------------------------------------------------")
    return curso_max, curso_min  # Devuelve los cursos

def horario_flexible(datos):
    cursos_horario_flexible = datos[datos['Schedule'].str.contains('Flexible schedule', case=False, na=False)]
    porcentaje_horario_flexible = round((len(cursos_horario_flexible) / len(datos)) * 100, 2)
    print("----------------------------------------------------------------")
    print("Porcentaje de cursos con horario flexible:\n", porcentaje_horario_flexible, '%')
    print("----------------------------------------------------------------")
    return porcentaje_horario_flexible  # Devuelve el porcentaje


# Suponiendo que ya tienes el DataFrame `datos` cargado
# datos = pd.read_csv("ruta_del_archivo.csv")  # Carga tu DataFrame aquí

# 1. Gráfica de barras que muestre el número de cursos en cada nivel de dificultad
def graficar_nivel_dificultad(datos):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=datos, x='Level', order=datos['Level'].value_counts().index)
    plt.title('Número de Cursos por Nivel de Dificultad')
    plt.xlabel('Nivel de Dificultad')
    plt.ylabel('Número de Cursos')
    plt.xticks(rotation=45)
    plt.show()

# 2. Gráfica de barras horizontal que muestre el número de cursos en las principales categorías
def graficar_categorias(datos):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=datos, y='Keyword', order=datos['Keyword'].value_counts().index)
    plt.title('Número de Cursos por Categoría')
    plt.xlabel('Número de Cursos')
    plt.ylabel('Categoría')
    plt.show()

# 3. Gráfico de dispersión para visualizar la relación entre la duración del curso y el número de revisiones
def graficar_duracion_revisiones(datos):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=datos, x='Duration', y='Review', alpha=0.6)
    plt.title('Relación entre Duración del Curso y Número de Revisiones')
    plt.xlabel('Duración del Curso')
    plt.ylabel('Número de Revisiones')
    plt.show()

# 4. Histograma de la distribución de las duraciones de los cursos
def graficar_histograma_duracion(datos):
    plt.figure(figsize=(10, 6))
    sns.histplot(datos['Duration'], bins=20, kde=True)
    plt.title('Distribución de la Duración de los Cursos')
    plt.xlabel('Duración del Curso')
    plt.ylabel('Frecuencia')
    plt.show()

# 5. Gráfico de cajas para visualizar la distribución de las calificaciones de los cursos por nivel de dificultad
def graficar_cajas_calificaciones(datos):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=datos, x='Level', y='Rating')
    plt.title('Distribución de Calificaciones por Nivel de Dificultad')
    plt.xlabel('Nivel de Dificultad')
    plt.ylabel('Calificación')
    plt.show()
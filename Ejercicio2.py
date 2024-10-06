import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("movie.csv")

# Ver los nombres de las columnas para asegurarnos de que la columna 'vote_average' existe
print(df.columns)

# Agrupar las películas por rangos de calificación
bins = [0, 2, 4, 6, 8, 10]  # Definir los límites de los rangos
labels = ['0-2', '2-4', '4-6', '6-8', '8-10']  # Etiquetas para los rangos
df['rating_range'] = pd.cut(df['vote_average'], bins=bins, labels=labels)

# Contar cuántas películas hay en cada rango de calificación
frecuencia = df['rating_range'].value_counts().sort_index()

# Verificar si hay datos antes de continuar
if not frecuencia.empty:
    # Crear el gráfico de líneas
    plt.figure(figsize=(10, 6))
    plt.plot(frecuencia.index, frecuencia.values, marker='o', linestyle='-', color='b')

    # Añadir etiquetas y título
    plt.xlabel('Rango de Calificaciones', fontsize=12)
    plt.ylabel('Cantidad de Películas', fontsize=12)
    plt.title('Distribución de Calificaciones Promedio en Películas', fontsize=15)

    plt.tight_layout()
    plt.show()
else:
    print("No hay suficientes datos en la columna 'vote_average'.")

'''
ANALISIS:

Las películas con rangos de calificaciones promedio más altos (8-10) 
son las que tienen mayor cantidad de calificaciones positivas. Esto puede 
indicar que estas películas son más populares y valiosas para el público en general.

Aqui esta el link del dataset:
https://www.kaggle.com/datasets/ayushi10kumari/top-rated-movie-dataset
'''
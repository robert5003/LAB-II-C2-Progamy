import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('iphone.csv')

# Convertir la columna 'date' a formato de fecha (si es necesario)
data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Eliminar filas donde no se pudo convertir la fecha correctamente
data = data.dropna(subset=['date'])

# Agrupar los datos por mes y calcular la media de 'ratingScore' para cada mes
data['month'] = data['date'].dt.to_period('M')  # Agrupar por mes
monthly_avg = data.groupby('month')['ratingScore'].mean()

# Crear el gráfico de barras usando los datos agrupados por mes
plt.figure(figsize=(10, 6))
monthly_avg.plot(kind='bar', color='skyblue', width=0.8)

# Añadir etiquetas y título
plt.xlabel('Fecha (Mes)', fontsize=12)
plt.ylabel('Puntuación Promedio', fontsize=12)
plt.title('Puntuaciones Promedio de Productos por Mes', fontsize=15)

# Rotar las etiquetas del eje X para que se vean mejor
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


'''
ANALISIS:

El gráfico muestra la puntuación promedio de productos iPhone por mes. 
Se puede observar que los meses con mayor puntuación promedio son los meses 
de enero y febrero, mientras que los meses con menor puntuación promedio son 
los meses de marzo y abril. Esto puede indicar que los usuarios de iPhone 
tienden a dar mejores puntajes a productos más recientes

Aqui esta el link del dataset:
https://www.kaggle.com/datasets/mrmars1010/iphone-customer-reviews-nlp
'''
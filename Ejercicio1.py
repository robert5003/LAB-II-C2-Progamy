import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Spotify Most Streamed Songs.csv')

# Ver los nombres de las columnas para asegurarse de que 'streams' exista
print(data.columns)

# Convertir la columna 'streams' a tipo numérico, forzando errores a NaN y luego eliminándolos
data['streams'] = pd.to_numeric(data['streams'], errors='coerce')

# Eliminar filas con valores NaN en 'streams'
data = data.dropna(subset=['streams'])

# Seleccionamos las 10 canciones más reproducidas, usando la columna 'streams'
top_10_songs = data.nlargest(10, 'streams')

# Crear el gráfico circular
plt.figure(figsize=(10, 8))
plt.pie(top_10_songs['streams'], labels=top_10_songs['track_name'], autopct='%1.1f%%', 
        startangle=140, 
        colors=['#ff9999','#66b3ff','#99ff99','#ffcc99',
                '#c2c2f0','#ffb3e6','#c4e17f','#76d7c4',
                '#f7b7a3','#aec6cf'])

plt.title('Top 10 Mejores Canciones por Streams en Spotify', fontsize=15)

plt.tight_layout()
plt.show()

'''
ANALISIS:
El gráfico refleja la gran popularidad de ciertas canciones que han marcado 
tendencias en los últimos años. Aunque "Blinding Lights" lidera claramente, 
las demás canciones del top 10 mantienen una distribución bastante uniforme, 
lo que indica que varios géneros y artistas han sido dominantes en la plataforma de Spotify.

Aquí este el link del dataset que se utilizó:
https://www.kaggle.com/datasets/abdulszz/spotify-most-streamed-songs/data
'''

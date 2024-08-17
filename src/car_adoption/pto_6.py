import pandas as pd

# Leer el archivo CSV en un DataFrame y establecer 'Country' como índice
df = pd.read_csv('D:/dev/tp_iglesias_2/files/EcarSalesByCountryAndYear.csv', index_col='Country')

# Identificar los últimos dos años disponibles
years = df.columns[-2:]  # Últimos dos años

# Calcular el crecimiento de las ventas entre los últimos dos años
df['Crecimiento'] = (df[years[1]] - df[years[0]]) / df[years[0]]

# Convertir el crecimiento a porcentaje
df['Crecimiento'] *= 100

# Redondear la columna 'Crecimiento' a 1 decimal
df['Crecimiento'] = df['Crecimiento'].round(1)

# Ordenar el DataFrame por la columna 'Crecimiento' de mayor a menor
df_sorted = df.sort_values(by='Crecimiento', ascending=False)

# Mostrar el DataFrame ordenado
print(df_sorted)

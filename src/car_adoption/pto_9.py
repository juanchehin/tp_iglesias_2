import pandas as pd

# Leer el archivo CSV en un DataFrame y establecer 'Country' como índice
df = pd.read_csv('D:/dev/tp_iglesias_2/files/EcarSalesByCountryAndYear.csv', index_col='Country')

# Crear el nuevo DataFrame 'df_Recent' con solo las columnas 'Sales 2021' y 'Sales 2020'
df_Recent = df[['Sales 2021', 'Sales 2020']]

# Calcular las ventas totales para 2020 y 2021
total_sales_2020 = df_Recent['Sales 2020'].sum()
total_sales_2021 = df_Recent['Sales 2021'].sum()

# Mostrar las ventas totales
print(f"Ventas totales en 2020: {total_sales_2020}")
print(f"Ventas totales en 2021: {total_sales_2021}")

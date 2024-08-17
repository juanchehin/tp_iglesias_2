import pandas as pd

# Leer el archivo CSV en un DataFrame y establecer 'Country' como índice
df = pd.read_csv('D:/dev/tp_iglesias_2/files/EcarSalesByCountryAndYear.csv', index_col='Country')

# Crear el nuevo DataFrame 'df_Recent' con solo las columnas 'Sales 2021' y 'Sales 2020'
df_Recent = df[['Sales 2021', 'Sales 2020']]

# Mostrar el nuevo DataFrame
print(df_Recent)

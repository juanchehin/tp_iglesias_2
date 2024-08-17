import pandas as pd

# Leer el archivo CSV en un DataFrame y establecer 'Country' como índice
df = pd.read_csv('D:/dev/tp_iglesias_2/files/EcarSalesByCountryAndYear.csv', index_col='Country')

# Crear el nuevo DataFrame 'df_Recent' con solo las columnas 'Sales 2021' y 'Sales 2020'
df_Recent = df[['Sales 2021', 'Sales 2020']]

# Filtrar el DataFrame para mostrar solo Estados Unidos y Canadá
df_Recent_filtered = df_Recent.loc[df_Recent.index.isin(['United States', 'Canada'])]

# Mostrar el DataFrame filtrado
print(df_Recent_filtered)

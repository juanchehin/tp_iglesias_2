import pandas as pd

# Leer el archivo CSV con los datos de ventas
df = pd.read_csv('D:/dev/tp_iglesias_2/files/EcarSalesByCountryAndYear.csv', index_col='Country')

# Leer el archivo CSV con la información de continentes
df_continent = pd.read_csv('CountryContinent.csv', index_col='Country')

# Unir los DataFrames por la columna 'Country'
df_combined = df.join(df_continent)

# Mostrar el DataFrame combinado
print(df_combined)

# Asegúrate de que los datos para 2022 están presentes en el DataFrame combinado
# Si no están presentes, el código no funcionará correctamente

# Calcular ventas totales por continente para 2021 y 2022
sales_by_continent = df_combined.groupby('Continent').agg({
    'Sales 2021': 'sum',
    'Sales 2022': 'sum'  # Asegúrate de que 'Sales 2022' está en el DataFrame
})

# Calcular el crecimiento de las ventas de 2022 frente a 2021
sales_by_continent['Crecimiento'] = ((sales_by_continent['Sales 2022'] - sales_by_continent['Sales 2021']) / sales_by_continent['Sales 2021']) * 100

# Redondear el crecimiento a 1 decimal
sales_by_continent['Crecimiento'] = sales_by_continent['Crecimiento'].round(1)

# Mostrar el crecimiento por continente
print(sales_by_continent[['Crecimiento']])

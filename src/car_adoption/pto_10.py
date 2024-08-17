import pandas as pd

# Leer el archivo CSV con los datos de ventas
df = pd.read_csv('D:/dev/tp_iglesias_2/files/EcarSalesByCountryAndYear.csv', index_col='Country')

# Leer el archivo CSV con la información de continentes
df_continent = pd.read_csv('CountryContinent.csv', index_col='Country')

# Unir los DataFrames por la columna 'Country'
df_combined = df.join(df_continent)

# Mostrar el DataFrame combinado
print(df_combined)

import matplotlib.pyplot as plt

# Calcular ventas totales por continente para cada año
sales_by_continent = df_combined.groupby('Continent').agg({
    'Sales 2020': 'sum',
    'Sales 2021': 'sum'
})

# Mostrar las ventas totales por continente
print(sales_by_continent)

# Visualizar las ventas por continente
sales_by_continent.plot(kind='bar', figsize=(10, 6))
plt.title('Ventas por Continente')
plt.ylabel('Ventas Totales')
plt.xlabel('Continente')
plt.xticks(rotation=45)
plt.legend(title='Año')
plt.tight_layout()

# Mostrar el gráfico
plt.show()

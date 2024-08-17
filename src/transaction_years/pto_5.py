import pandas as pd

# Leer el archivo sales.csv en un DataFrame
df = pd.read_csv('D:/dev/tp_iglesias_2/files/sales.csv')

# Crear una tabla dinámica con totales de filas y columnas (margins=True)
pivot_table = pd.pivot_table(df, values='cantidad de productos comprados', 
                             index='ID del producto', columns='región', 
                             aggfunc='sum', margins=True)

# Mostrar la tabla dinámica
print(pivot_table)

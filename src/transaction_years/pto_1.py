import pandas as pd

# Leer el archivo sales.csv en un DataFrame
df = pd.read_csv('D:/dev/tp_iglesias_2/files/sales.csv')

# Mostrar las primeras filas del DataFrame para verificar la carga de los datos
print(df.head())

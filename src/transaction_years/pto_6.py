import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo sales.csv en un DataFrame
df = pd.read_csv('sales.csv')

# Crear la tabla dinámica con totales
pivot_table = pd.pivot_table(df, values='cantidad de productos comprados', 
                             index='ID del producto', columns='región', 
                             aggfunc='sum', margins=True)

# Excluir los totales de filas y columnas
pivot_table_filtered = pivot_table.drop(index='All').drop(columns='All')

# Crear un gráfico de barras horizontales apiladas
pivot_table_filtered.plot(kind='barh', stacked=True)

# Mostrar el gráfico
plt.xlabel('Cantidad de productos comprados')
plt.ylabel('ID del producto')
plt.title('Ventas por Producto y Región (Apiladas)')
plt.show()

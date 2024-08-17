import pandas as pd

# Especifica la ruta del archivo .xlsx
archivo_excel = 'D:/dev/tp_iglesias_2/files/EcarSalesByCountryAndYear2.xlsx'

# Cargar las dos pestañas del archivo .xlsx
documentacion_df = pd.read_excel(archivo_excel, sheet_name='Documentación')
ventas_df = pd.read_excel(archivo_excel, sheet_name='EcarSalesByCountryAndYear')

# Mostrar el contenido de los DataFrames
print("Documentación:")
print(documentacion_df.head())

print("\nVentas por país y año:")
print(ventas_df.head())

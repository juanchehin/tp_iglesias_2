# 3. Refine the call used in step #2 to set the index to Country (use the sheet_name and index_col parameters)

import pandas as pd

# Especifica la ruta del archivo .xlsx
archivo_excel = 'D:/dev/tp_iglesias_2/files/EcarSalesByCountryAndYear2.xlsx'

# Cargar la pestaña 'EcarSalesByCountryAndYear' y establecer el índice en la columna 'País'
ventas_df = pd.read_excel(archivo_excel, sheet_name='EcarSalesByCountryAndYear', index_col='País')

# Mostrar el contenido del DataFrame
print(ventas_df.head())

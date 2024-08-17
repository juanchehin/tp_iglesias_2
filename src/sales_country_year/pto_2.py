# 2. Refine the call to read_excel() to read the worksheet tab 
# 'EcarSalesByCountryAndYear into a DataFrame (use the sheet_name parameter)

import pandas as pd

# Especifica la ruta del archivo .xlsx
archivo_excel = 'D:/dev/tp_iglesias_2/files/EcarSalesByCountryAndYear2.xlsx'

# Cargar solo la pestaña 'EcarSalesByCountryAndYear' del archivo .xlsx
ventas_df = pd.read_excel(archivo_excel, sheet_name='EcarSalesByCountryAndYear')

# Mostrar el contenido del DataFrame
print(ventas_df.head())

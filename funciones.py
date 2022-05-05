import pandas as pd

#Leemos el csv
df = pd.read_csv('USA_Housing.csv', delimiter = ',', encoding='UTF-8')
#Estas son las columnas que tiene nuestro csv
print('-------------Columnas del csv-----------')
print(df.columns)
#Vamos a traducir las columnas, es decir, vamos a cambiar sus nombres para que nos sea más fácil trabajar con ellas
print('--------------Traducción de las columnas----------------')
df.rename(columns= {'Price': 'precio', 'Address': 'direccion', 'Avg. Area Income': 'media salario', 'Avg. Area House Age':
    'media antugüedad casas', 'Avg. Area Number of Rooms': 'media número habitaciones', 'Avg. Area Number of Bedrooms': 'media número dormitorios por casa', 'Area Population':'población'}, inplace=True)
print(df.columns)

print('------------Datos del csv-------------')
print(df.head()) 
print(df.tail())
'''Se usa para poder ver las primeras filas de nuestros datos y ver los distintos valores que tenemos asociados a las columnas. 
Lo mismo con el .tail(), lo único que nos mostrará las últimas filas. Podemos usar ambos para ver los datos, aunque es más común el .head()'''

print('----------Descripción e información del csv----------------')
print(df.describe())
print(df.info())
'''
El .describe(), no enseña en una columna los datos más relevantes que necesitamos saber sobre este DataSet, incluye 
la media, la desviación típica, los cuartiles uno, dos y tres, el mínimo, el máximo
'''
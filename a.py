import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Leemos el csv
df = pd.read_csv('USA_Housing.csv', delimiter = ',', encoding='UTF-8')

df.rename(columns= {'Price': 'precio', 'Address': 'direccion', 'Avg. Area Income': 'media-salario', 'Avg. Area House Age':
    'media-antiguedad-casa', 'Avg. Area Number of Rooms': 'media-numero-habitaciones', 'Avg. Area Number of Bedrooms': 'media-numero-dormitorios-casas', 'Area Population':'poblacion'}, inplace=True)

bins = [2, 4, 6, 8, 10]
nombres = ['2-4', '4-6', '6-8', '8-10']
df['media-antiguedad-casa'] = pd.cut(df['media-antiguedad-casa'], bins, labels = nombres)
df2 = df.groupby('media-antiguedad-casa').mean()
df3= df.groupby('media-antiguedad-casa').count()
df4 = df2[['precio', 'poblacion', 'media-salario']]
df5 = df2[['media-numero-habitaciones', 'media-numero-dormitorios-casas']]
df3.rename(columns={'precio': 'numeroVivienda'}, inplace = True)
plt.subplots()
plt.bar(df2.index, df2['precio'])

plt.show()
print(df2.index)
print(df2.columns)
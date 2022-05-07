import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Leemos el csv
df = pd.read_csv('USA_Housing.csv', delimiter = ',', encoding='UTF-8')
#Estas son las columnas que tiene nuestro csv
print('-------------Columnas del csv-----------')
print(df.columns)
print('\n')

#Vamos a traducir las columnas, es decir, vamos a cambiar sus nombres para que nos sea más fácil trabajar con ellas
print('--------------Traducción de las columnas----------------')
df.rename(columns= {'Price': 'precio', 'Address': 'direccion', 'Avg. Area Income': 'media salario', 'Avg. Area House Age':
    'media antigüedad casas', 'Avg. Area Number of Rooms': 'media número habitaciones', 'Avg. Area Number of Bedrooms': 'media número dormitorios por casa', 'Area Population':'población'}, inplace=True)
print(df.columns)

print('\n')
print('------------Datos del csv-------------')
print(df.head()) 
print(df.tail())
'''Se usa para poder ver las primeras filas de nuestros datos y ver los distintos valores que tenemos asociados a las columnas. 
Lo mismo con el .tail(), lo único que nos mostrará las últimas filas. Podemos usar ambos para ver los datos, aunque es más común el .head()'''

print('\n')
print('----------Descripción e información del csv----------------')
print(df.describe())
print(df.info())
'''
El .describe(), no enseña en una columna los datos más relevantes que necesitamos saber sobre este DataSet, incluye 
la media, la desviación típica, los cuartiles uno, dos y tres, el mínimo, el máximo y la cantidad de datos que tenemos. 
Nos lo realiza de cada columna de manera individual, lo cual es bastante útil para hacer una comparativa entre ellas.

El .info(), nos mostrará en una columna la descripción básica de los datos, es decir, el tipo (float, integrer, string, etc.),
el número de valores de cada columna y si son nulos.
'''
print('\n')
print('----------Clasificación de las variables--------------')
print('Variables categóricas: dirección')
print('Variables numéricas: precio, media salario, media antigüedad casas, media número habitaciones,media número dormitorios por casa, población')
'''
Esta clasificación la haremos basándonos en la información que nos ha dado el .info().
Las variables categóricas son todas aquellas que no son numéricas, es decir, que nos dan una descripción mediante palabras o símbolos.
Si nos fijamos en lo que nos ha mostrado .info(), aquí podemos ver que dirección lo ha reconocido como un objeto, donde nos cabría la duda de si es un objeto numérico o no. Al ver
los datos de dicha columna vemos con claridad que tiene que ir en la parte categórica, al ser una indentificación del lugar.
Las variables numéricas son datos numéricos, como integrers, float, etc.
'''

print('\n')
print('------------Análisis de las variables categóricas----------------')
def bar_plt(variable):
    var = df[variable]
    varValue = var.value_counts() #nos va a contar los datos en función de cada columna
    
    plt.figure(figsize=(9, 3)) #tamaño de la ventana
    plt.bar(varValue.index, varValue) #Es un diagrama de barras
    plt.xticks(varValue.index, varValue.index.values) #etiquetas
    plt.ylabel('Frecuencia')
    plt.tittle(variable)
    plt.show()
    
    print("{}:\n{}".format(variable, varValue))
    
'''
La función nos sirve para poder mostrar y comparar las variables que son categóricas, 
pero al solo tener una, no la podemos comparar non ninguna otra. Por eso esta función no 
se usará en este fichero.
'''

print('\n')

def calculomedia(variable):
    m =  df[variable].sum()/df[variable].count()
    return m

def calculovarianza(variable, media):
    v = ((df[variable] - media)**2).sum()/(df[variable].count())
    return v
'''
Calculamos unos datos estadísticos de cada columna para que nos facilite la comparación entre los datos 
y nos proporcione más información
'''
def histograma(variable, media, desviacion_tipica, varianza):
    min = df[variable].min()
    max = df[variable].max()
    if media < 10:
        a = 0.01
    else:
        a = 1
    x = np.arange(min, max, a)
    f = 1/(desviacion_tipica * np.sqrt(2*np.pi)) * np.exp(-(x - media) ** 2/(2 * varianza))
    fig, ax1 = plt.subplots()
    ax1.hist(df[variable], bins= 50)
    ax2 = ax1.twinx()
    ax2.plot(x, f, color = 'black', linestyle = 'dashed', linewidth=3)
    plt.title('Histograma de {}'.format(variable))
    plt.axvline(media, color='red', linestyle='dashed', linewidth=1,label = str(media))
    plt.legend(loc='upper right')
    plt.savefig('img/Histograma de {}'.format(variable) + '.png', bbox_inches='tight')
    plt.show()
'''
Tras ver estos histogramas podemos apreciar que algunas de las variables numérica tienen una distribución simétrica, 
es decir, se asemeja a la campana de Gauss. Los gráficos que hemos podido ver esto es en la variable media salario.
El resto de valores, salvo la media antigüedad casas y media número dormitorios por casa, presenta simetría pero no 
la suficiente como para llegar a considerarse una campana de Gauss.



'''

numericVar = ['precio', 'media salario', 'media antigüedad casas', 'media número habitaciones','media número dormitorios por casa', 'población']
for n in numericVar:
    media = round(calculomedia(n), 2)
    varianza = round(calculovarianza(n, media), 2)
    desviacion_tip = round((varianza**(1/2)), 2)
    print(desviacion_tip)
    print(df[n].describe())
    print('\n')
    histograma( n, media, desviacion_tip, varianza)


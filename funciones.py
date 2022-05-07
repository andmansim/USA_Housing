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
df.rename(columns= {'Price': 'precio', 'Address': 'direccion', 'Avg. Area Income': 'media-salario', 'Avg. Area House Age':
    'media-antigüedad-casa', 'Avg. Area Number of Rooms': 'media-numero-habitaciones', 'Avg. Area Number of Bedrooms': 'media-numero-dormitorios-casas', 'Area Population':'poblacion'}, inplace=True)
print(df.columns)

print('\n')
print('------------Datos del csv-------------')
print('Primeras filas')
print(df.head())
print('\n') 
print('Últimas filas')
print(df.tail())
'''Se usa para poder ver las primeras filas de nuestros datos y ver los distintos valores que tenemos asociados a las columnas. 
Lo mismo con el .tail(), lo único que nos mostrará las últimas filas. Podemos usar ambos para ver los datos, aunque es más común el .head()'''

print('\n')
print('----------Descripción e información del csv----------------')
print('Descripción:')
print(df.describe())
print('\n')
print('Información datos')
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
print('Variables numéricas: precio, media-salario, media-antigüedad-casa, media-numero-habitaciones,media-numero-dormitorios-casas, poblacion')
'''
Esta clasificación la haremos basándonos en la información que nos ha dado el .info().
Las variables categóricas son todas aquellas que no son numéricas, es decir, que nos dan una descripción mediante palabras o símbolos.
Si nos fijamos en lo que nos ha mostrado .info(), aquí podemos ver que dirección lo ha reconocido como un objeto, donde nos cabría la duda de si es un objeto numérico o no. Al ver
los datos de dicha columna vemos con claridad que tiene que ir en la parte categórica, al ser una indentificación del lugar.
Las variables numéricas son datos numéricos, como integrers, float, etc.
'''
print('\n')
print('------------Análisis de las variables categóricas----------------')
print('Como solo tenemos una variable categórica no podremos hacer una comparación.')
print('\n')

print('-----------Identificar valores nulos-----------')
nulos = df.isnull().sum()
print(nulos)
print('\n')

def bar_plt(df, variable):
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

def calculomedia(df, variable):
    m =  (df[variable].sum())/(df[variable].count())
    return m

def calculovarianza(df, variable, media):
    v = ((df[variable] - media)**2).sum()/(df[variable].count())
    return v

'''
Calculamos unos datos estadísticos de cada columna para que nos facilite la comparación entre los datos 
y nos proporcione más información
'''

#Representación de cada variable numérica
'''print('------------Análisis de las variables numérica----------------')'''
def histograma(df, variable, media, desviacion_tipica, varianza, min, max):

    if media < 10:
        a = 0.01
    else:
        a = 1
    x = np.arange(min, max + a, a)
    f = 1/(desviacion_tipica * np.sqrt(2*np.pi)) * np.exp(-(x - media) ** 2/(2 * varianza))
    fig, ax1 = plt.subplots()
    ax1.hist(df[variable], bins= 50)
    ax2 = ax1.twinx()
    ax2.plot(x, f, color = 'black', linestyle = 'dashed', linewidth=3)
    plt.title('Histograma de {}'.format(variable))
    plt.axvline(media, color='red', linestyle='dashed', linewidth=1,label = str(media))
    plt.legend(loc='upper right')
    plt.savefig('img/Histograma-de-{}'.format(variable) + '.png', bbox_inches='tight')
    plt.show()


#valores atípicos
def criterioDeTukey(df, variable, primerCuartil, tercerCuartil):
    
    valoresAberrantesInferiores = []
    valoresAberrantesSuperiores = []
    ordenar =df[variable].sort_values()
    intercuartil = tercerCuartil - primerCuartil
    limiteInferior = primerCuartil - (1.5 * intercuartil)
    limiteSuperior = tercerCuartil + (1.5 * intercuartil)

    for valorObservacion in ordenar:
        if valorObservacion < limiteInferior:
            valoresAberrantesInferiores.append(valorObservacion)

        if valorObservacion > limiteSuperior:
            valoresAberrantesSuperiores.append(valorObservacion)

    valoresAberrantes = valoresAberrantesInferiores + valoresAberrantesSuperiores

    return (valoresAberrantes)

    
#comparamos: precio-antigüedad, precio-habitaciones, direccion-poblacion, poblacion-precio, habitaciones-dormitorios
def graficas(df):
    bins = [2, 4, 6, 8, 10]
    nombres = ['2-4', '4-6', '6-8', '8-10']
    df['media-antigüedad-casa'] = pd.cut(df['media-antigüedad-casa'], bins, labels = nombres)
    df2 = df.groupby('media-antigüedad-casa').mean()
    df3= df.groupby('media-antigüedad-casa').count()
    df4 = df2[['precio', 'poblacion', 'media-salario']]
    df5 = df2[['media-numero-habitaciones', 'media-numero-dormitorios-casas']]
    df3.rename(columns={'precio': 'numeroVivienda'}, inplace = True)
    plt.subplots()
    plt.xlabel('Número de viviendas por rango de años')
    x = df3['numeroVivienda']
    plt.pie(x, autopct="%0.1f %%", labels=nombres)
    plt.savefig('img/Número-viviendas-por-años' + '.png', bbox_inches='tight')
    
    df4.plot(kind='bar')
    plt.title('Relación precio/población con la antigüedad casas')
    plt.savefig('img/Relación-precio-población-con-antigüedad' + '.png', bbox_inches='tight')
    
    df5.plot(kind='bar')
    plt.title('Relación habitaciones, dormitorios y salario con la antigüedad casas')
    plt.savefig('img/Relación-habitaciones-dormitorios-salario-con-antigüedad' + '.png', bbox_inches='tight')
    plt.show()

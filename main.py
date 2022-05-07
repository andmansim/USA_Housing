import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Leemos el csv
df = pd.read_csv('USA_Housing.csv', delimiter = ',', encoding='UTF-8')

#Estas son las columnas que tiene nuestro csv
print('-------------Columnas del csv-----------')
print(df.columns)
print('\n')

'''**********************************************************************************************************
Index(['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population', 'Price', 'Address'],
      dtype='object')
**********************************************************************************************************'''


#Vamos a traducir las columnas, es decir, vamos a cambiar sus nombres para que nos sea más fácil trabajar con ellas
print('--------------Traducción de las columnas----------------')
df.rename(columns= {'Price': 'precio', 'Address': 'direccion', 'Avg. Area Income': 'media-salario', 'Avg. Area House Age':
    'media-antig-casa', 'Avg. Area Number of Rooms': 'media-numero-habitaciones', 'Avg. Area Number of Bedrooms': 'media-numero-dormitorios-casas', 'Area Population':'poblacion'}, inplace=True)
print(df.columns)
df_or = df.copy() 
print('\n')
'''
***************************************se quedan con estos nombres********************************
Index(['media-salario', 'media-antig-casa', 'media-numero-habitaciones',
       'media-numero-dormitorios-casas', 'poblacion', 'precio', 'direccion'],
      dtype='object')
**************************************************************************************************'''

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
'''
*******************************************************************************************************************
Descripción:
       media-salario  media-antig-casa  media-numero-habitaciones  media-numero-dormitorios-casas     poblacion        precio
count    5000.000000       5000.000000                5000.000000                     5000.000000   5000.000000  5.000000e+03
mean    68583.108984          5.977222                   6.987792                        3.981330  36163.516039  1.232073e+06
std     10657.991214          0.991456                   1.005833                        1.234137   9925.650114  3.531176e+05
min     17796.631190          2.644304                   3.236194                        2.000000    172.610686  1.593866e+04
25%     61480.562388          5.322283                   6.299250                        3.140000  29403.928702  9.975771e+05
50%     68804.286404          5.970429                   7.002902                        4.050000  36199.406689  1.232669e+06
75%     75783.338666          6.650808                   7.665871                        4.490000  42861.290769  1.471210e+06
max    107701.748378          9.519088                  10.759588                        6.500000  69621.713378  2.469066e+06
************************************************************************************************************
'''
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
print('Variables numéricas: precio, media-salario, media-antig-casa, media-numero-habitaciones,media-numero-dormitorios-casas, poblacion')

'''**********************************Información datos*************************************************************+
RangeIndex: 5000 entries, 0 to 4999
Data columns (total 7 columns):
 #   Column                          Non-Null Count  Dtype
---  ------                          --------------  -----
 0   media-salario                   5000 non-null   float64
 1   media-antig-casa                5000 non-null   float64
 2   media-numero-habitaciones       5000 non-null   float64
 3   media-numero-dormitorios-casas  5000 non-null   float64
 4   poblacion                       5000 non-null   float64
 5   precio                          5000 non-null   float64
 6   direccion                       5000 non-null   object
dtypes: float64(6), object(1)
*********************************************************************************************************'''
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
'''
********************************************************************************
-----------Identificar valores nulos-----------
media-salario                     0
media-antig-casa                  0
media-numero-habitaciones         0
media-numero-dormitorios-casas    0
poblacion                         0
precio                            0
direccion                         0
**********************************************************************************
'''
'''No hay ningún valor nulo.
'''

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
pero al solo tener una, no la podemos comparar con ninguna otra. Por eso esta función no 
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
y nos proporcione más información.
'''

#Representación de cada variable numérica
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

'''
Nos muesta distintas gráficas donde las analizaremos. Se explica más adelante, cuando se llama a la función.
'''
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

'''
Esta función seguirá el criterio de Turkey para ver que valores son atípicos, es decir, cuales se alejan demasiado de 
la media. Para ello, calcularemos los cuartiles y veremos su rango para después calcular el límite inferior y superior. 
Cualquier valor que se salga de estos límites se considerará atípico.
'''

def graficas(df):
    bins = [2, 4, 6, 8, 10]
    nombres = ['2-4', '4-6', '6-8', '8-10']
    
    df['media-antig-casa'] = pd.cut(df['media-antig-casa'], bins, labels = nombres)
    df2 = df.groupby('media-antig-casa').mean()
    df3= df.groupby('media-antig-casa').count()
    df4 = df2[['precio', 'poblacion', 'media-salario']]
    df5 = df2[['media-numero-habitaciones', 'media-numero-dormitorios-casas']]
    df3.rename(columns={'precio': 'numeroVivienda'}, inplace = True)
    plt.subplots()
    plt.xlabel('Número de viviendas por rango de años')
    x = df3['numeroVivienda']
    plt.pie(x, autopct="%0.1f %%", labels=nombres)
    plt.savefig('img/Número-viviendas-por-años' + '.png', bbox_inches='tight')
    
    df4.plot(kind='bar')
    plt.title('Relación precio/población/salario con la antig casas')
    plt.savefig('img/Relación-precio-población-salario-con-antig' + '.png', bbox_inches='tight')
    
    df5.plot(kind='bar')
    plt.title('Relación habitaciones y dormitorios con la antig casas')
    plt.savefig('img/Relación-habitaciones-dormitorios-con-antig' + '.png', bbox_inches='tight')
    
    plt.show()
   
'''
Muestra unos gráficos, cuya conclusión se explica más adelante, cuando se llama a la función.
'''

numericVar = ['precio', 'media-salario', 'media-antig-casa', 'media-numero-habitaciones','media-numero-dormitorios-casas', 'poblacion']
print('------------Análisis de las variables numéricas----------------')

for n in numericVar:
    min = df[n].min()
    max = df[n].max()
    media = round(calculomedia(df, n), 2)
    varianza = round(calculovarianza(df, n, media), 2)
    desviacion_tip = round((varianza**(1/2)), 2)
    q1 = np.percentile(df[n], 25)
    q2 = np.percentile(df[n], 50)
    q3 = np.percentile(df[n], 75)
    atipicos = criterioDeTukey(df, n, q1, q3)
    #Enseñamos aquellos valores que hacen que nuestra distribución varie tanto
    print('Los valores atípicos de {}'.format(n) + ' son: ' + str(len(atipicos)) + '\n')
    
    histograma( df, n, media, desviacion_tip, varianza, min, max)
    '''
    Se generan los histogramas:
    -Histograma-de-media-antig-casa.png--> muestra la antiguedad de las viviendas
    -Histograma-de-media-numero-dormitorios-casas.png--> muestra la distribución de los dormitorios por viviendas
    -Histograma-de-media-numero-habitaciones.png--> muestra la distribución de las habitaciones por vivienda
    -Histograma-de-media-salario.png--> muestra la distribución del salario 
    -Histograma-de-poblacion.png--> muestra la distribución de la población
    -Histograma-de-precio.png --> muestra la distribución de precios
    Tras ver estos histogramas podemos apreciar que algunas de las variables numéricas tienen una distribución simétrica, 
    es decir, se asemejan a la campana de Gauss. El gráfico en el que hemos podido ver esto, es el de la media-salario.
    El resto de valores, salvo la media-antig-casa y media-numero-dormitorios-casas, presenta simetría pero no 
    la suficiente como para llegar a considerarse una campana de Gauss.
    Con todo esto podemos apreciar que según van avanzando los datos cada vez hay menos repeticiones. 

    Ahora vamos a analizar las variables de manera individual, viendo algunas caracteríaticas de ellas:

    1º Precio: Su distribución encaja con la campana de Gauss, es decir, la mayoría de los precios del mercado suelen mantenerse estandar (en torno a la media). 
    Su media está en torno al millón de euros.

    2º Media-salario, es la que más se asemeja a la campana, dado que ningún valor se excede de dicha distribución. Por tanto, pasa 
    algo parecido al precio. La mayoría tiene un salario, muy cercano a la media, que es de unos 68 mil euros.

    3º media-antig-casa, la antigüedad de la mayor parte de las viviendas, está entre los 5 y 7 años, y se aprecia una bajada significativa de nuevas viviendas
    hace 6 años.

    4º Media número de habitaciones, la media ronda por las 7 habitaciones por casa, pero algunas casas llegan a tener 8 habitaciones. 

    5º media-numero-dormitorios-casas, los datos se agrupan mediante intervalos perfectamente marcados, por lo cual, 
    es imposible que presente simetría y tenga algún parecido con la campana. También podemos apreciar que la gran mayoría de casas
    contienen 2 o 3 dormitorios.

    6º poblacion, la media de personas que viven en un área es de 40000.

    '''
     
#Comparando varios datos  
graficas(df)
'''
Para este análisis, se han agrupado los datos por rangos de antigüedad de las viviendas, en este caso, se han tomado datos bianuales:
2-4, 4-6, 6-8. 8-10
Se han realizado tres gráficos para analizar distintos valores:
-En el gráfico Histograma-de-media-antig-casa.png, vemos el número de casas por año representado por porcentajes, mediante un diagrama de sectores.
Podemos apreciar que hay muchas menos casas nuevas que antigüas.
-En el gráfico Relación-habitaciones-dormitorios-con-antig.png podemos ver que hay un mayor número de habitaciones en las casas más nuevas, lo mismo pasa con el 
número de dormitorios, aunque la diferencia no es tan grande. 
***********************************************************************************************
  
media-antig-casa        media-numero-habitaciones         media-numero-dormitorios-casas
2-4                                7.166943                        4.033482
4-6                                6.958544                        3.960192
6-8                                7.014428                        3.998959
8-10                               6.889425                        4.024404
*************************************************************************************************
-En e gráfico Relación-precio-población-salario-con-antig.png, tenemos una situación completamente opuesta, se puede apreciar una gran diferencia de 
precio según avanzan los años, en cambio, el salario y la población se mantienen más o menos constantes.
**********************************************************************
media-antig-casa  precio        poblacion      media-salario
2-4               8.683925e+05  36308.331526   68328.508976
4-6               1.107975e+06  36113.830415   68448.974241
6-8               1.361791e+06  36280.652647   68687.749984
8-10              1.611785e+06  34620.994657   69612.857176
**********************************************************************
'''
#Incremento del número de viviendas por año
bins=[2,3,4,5,6,7,8,9,10]
nombres= ['3', '4', '5', '6', '7', '8', '9', '10']

df_or['media-antig-casa'] = pd.cut(df_or['media-antig-casa'], bins, labels = nombres)
df_or2 = df_or.groupby('media-antig-casa').mean()
df_or3= df_or.groupby('media-antig-casa').count()
df_or3.rename(columns={'precio': 'numeroViviendas'}, inplace = True)
df_or3['incrementoAnual'] = round(df_or3.numeroViviendas.pct_change() * 100, 2)
df_or3['incrementoAnual'][0]=0
grafica = plt.bar(df_or3.index, df_or3['incrementoAnual'])
print (df_or3['numeroViviendas'],df_or3['incrementoAnual'])
w = 0

for p in grafica:
    width= p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    plt.text(x + width/2, y + height*1.01, str(df_or3.incrementoAnual[w]) + '%', ha = 'center', weight = 'bold')
    w = w + 1
plt.title('Incremento de viviendas por año')
plt.savefig('img/IncrementoAnual' + '.png', bbox_inches='tight')   
plt.show()

'''
En esta gráfica 'IncrementoAnual.png', vemos el incremento anual en porcentaje del número de viviendas.
El mayor incremento de viviendas, se produce entre las que tienen una antigüedad de 3-4 años (identificados son la etiqueta '4')
Se ve, que el número de viviendas sigue decreciendo respecto del año anterior, hasta llegar a ser valores muy pequeños comparamdo con los años anteriores.

****************************************************************************************
ant       %     num 
3        0.00     5
4     2040.00   107 
5      550.47   696
6      151.29  1749
7       -4.63  1668
8      -60.07   666
9      -84.08   106
10     -97.17     3
******************************************************************************************
'''


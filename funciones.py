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
    x = np.arange(min, max + a, a)
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
Tras ver estos histogramas podemos apreciar que algunas de las variables numéricas tienen una distribución simétrica, 
es decir, se asemejan a la campana de Gauss. El gráfico en el que hemos podido ver esto, es el de la media salario.
El resto de valores, salvo la media antigüedad casas y media número dormitorios por casa, presenta simetría pero no 
la suficiente como para llegar a considerarse una campana de Gauss.
Con todo esto podemos apreciar que según van avanzando los datos cada vez hay menos repeticiones. 

Ahora vamos a analizar las variables de manera individual, viendo algunas caracteríaticas de ellas:


1º Precio: Su distribución encaja con la campana de Gauss, es decir, la mayoría del precio del mercado suele mantenerse estandar, 
para que sea más o menos asequible para todos los usuarios. 


2º Media salario, es la que más se asemeja a la campana, dado que ningún valor se excede de dicha distribución. Por tanto, pasa 
algo parecido al precio.


3º Media antigüedad casas, la mayoría de las casas rondan por los 5 o 7 años, auqnue tuvo una bajada hace 6 años.


4º Media número de habitaciones, la media ronda por las 7 habitaciones por casa, pero algunas casas llegan a tener 8 habitaciones. 


5º Media número dormitorios por casa, los datos se agrupan mediante intervalos perfectamente marcados, lo cual, 
es imposible que presente simetría y tenga algún parecido con la campana. También podemos apreciar que la gran mayoría de casas
contienen 2 o 3 dormitorios.

6º Población, la media de personas que viven en un área es de 40000.

'''

#valores atípicos
def criterioDeTukey(variable, primerCuartil, tercerCuartil):
    
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


numericVar = ['precio', 'media salario', 'media antigüedad casas', 'media número habitaciones','media número dormitorios por casa', 'población']
for n in numericVar:
    media = round(calculomedia(n), 2)
    varianza = round(calculovarianza(n, media), 2)
    desviacion_tip = round((varianza**(1/2)), 2)
    q1 = np.percentile(df[n], 25)
    q2 = np.percentile(df[n], 50)
    q3 = np.percentile(df[n], 75)
    atipicos = criterioDeTukey(n, q1, q3)
    #Enseñamos aquellos valores que hacen que nuestra distribución varie tanto
    print('Los valores atípicos de {}'.format(n) + ' son: ' + str(len(atipicos)) + '\n')
    #histograma( n, media, desviacion_tip, varianza)
    
#comparamos: precio-antigüedad, precio-habitaciones, direccion-poblacion, población-precio, habitaciones-dormitorios
def graficas(variable1, variable2):
    q1_v1 = np.percentile(df[variable1], 25)
    q2_v1 = np.percentile(df[variable1], 50)
    q3_v1 = np.percentile(df[variable1], 75)
    fig, ax1 = plt.subplots()
    l1 = []
    l2 = []
    l4 = []
    l5 = []
    for i in df[variable1]:
        if i < q1:
            l1.append(i)
        if q1 < i < media:
            l2.append(i)
        if  q2 < i < q3:
            l4.append(i)
        if i> q3:
            l5.append(i)
    print(l1)
    print(l2)
    
    ax1.plot(l1, color='black', linewidth=3)
    #ax2 = ax1.twinx()
    #ax2.plot(df[variable2], color='red', linewidth=3 )
    plt.title('Gráfica de {}'.format(variable1) + ' y {}'.format(variable2))
    plt.savefig('img/Gráfica de {}'.format(variable1) + ' y {}'.format(variable2) + '.png', bbox_inches='tight')
    plt.show()
    
graficas('precio', 'media antigüedad casas')
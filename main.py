from funciones import*

if __name__ =='__main__':
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
    
    numericVar = ['precio', 'media-salario', 'media-antigüedad-casa', 'media-numero-habitaciones','media-numero-dormitorios-casas', 'poblacion']
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
        Tras ver estos histogramas podemos apreciar que algunas de las variables numéricas tienen una distribución simétrica, 
        es decir, se asemejan a la campana de Gauss. El gráfico en el que hemos podido ver esto, es el de la media-salario.
        El resto de valores, salvo la media-antigüedad-casa y media-numero-dormitorios-casas, presenta simetría pero no 
        la suficiente como para llegar a considerarse una campana de Gauss.
        Con todo esto podemos apreciar que según van avanzando los datos cada vez hay menos repeticiones. 

        Ahora vamos a analizar las variables de manera individual, viendo algunas caracteríaticas de ellas:


        1º Precio: Su distribución encaja con la campana de Gauss, es decir, la mayoría del precio del mercado suele mantenerse estandar, 
        para que sea más o menos asequible para todos los usuarios. Su media es de 1 millón de euros.


        2º Media-salario, es la que más se asemeja a la campana, dado que ningún valor se excede de dicha distribución. Por tanto, pasa 
        algo parecido al precio. La mayoría tiene 68 mil euros.


        3º media-antigüedad-casa, la mayoría de las casas rondan por los 5 o 7 años, auqnue tuvo una bajada hace 6 años.


        4º Media número de habitaciones, la media ronda por las 7 habitaciones por casa, pero algunas casas llegan a tener 8 habitaciones. 


        5º media-numero-dormitorios-casas, los datos se agrupan mediante intervalos perfectamente marcados, lo cual, 
        es imposible que presente simetría y tenga algún parecido con la campana. También podemos apreciar que la gran mayoría de casas
        contienen 2 o 3 dormitorios.

        6º poblacion, la media de personas que viven en un área es de 40000.

        '''
    
    graficas(df)
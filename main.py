from funciones import*

if __name__ =='__main__':
    numericVar = ['precio', 'media-salario', 'media-antigüedad-casa', 'media-numero-habitaciones','media-numero-dormitorios-casas', 'poblacion']
    for n in numericVar:
        min = df[n].min()
        max = df[n].max()
        media = round(calculomedia(n), 2)
        varianza = round(calculovarianza(n, media), 2)
        desviacion_tip = round((varianza**(1/2)), 2)
        q1 = np.percentile(df[n], 25)
        q2 = np.percentile(df[n], 50)
        q3 = np.percentile(df[n], 75)
        atipicos = criterioDeTukey(n, q1, q3)
        #Enseñamos aquellos valores que hacen que nuestra distribución varie tanto
        print('Los valores atípicos de {}'.format(n) + ' son: ' + str(len(atipicos)) + '\n')
        histograma( n, media, desviacion_tip, varianza, min, max)
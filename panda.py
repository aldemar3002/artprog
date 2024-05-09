#linea para arrancar el código: python3 panda.py
# %%
import pandas as pd 
# %%
#carga el archivo 
df  = pd.read_csv ("housing.csv")

#muestra primeras ileras
print (df.head(3))

#MT = df [['longitude,latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value','ocean_proximity']].iloc[:2] #lo mismo al de despues pero mas caro
#print (df.head(12)[['longitude,latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value','ocean_proximity']]) #lo mismo pero mas barato

# Verificar la cantidad de datos y las variables
print("Cantidad de datos:", df.shape[0])
print("Variables:", df.shape[1])

# Identificar el tipo de variables
print(df.dtypes)

# Obtener estadísticas descriptivas
print(df.describe())






#moda = df.mode()
#media = df.

#moda_lo = moda['longitude'].iloc[0]
#moda_la = moda['latitude'].iloc[0]
#moda_ho = moda['housing_median_age'].iloc[0]
#moda_Tr = moda['total_rooms'].iloc[0]
#moda_Tb = moda['total_bedrooms'].iloc[0]
#moda_P = moda['population'].iloc[0]
#moda_hh = moda['households'].iloc[0]
#moda_mi = moda['median_income'].iloc[0]
#moda_mh = moda['median_house_value'].iloc[0]
#moda_op = moda['ocean_proximity'].iloc[0]

#print (la media de los valores es: , media)
#print (la moda se presenta de longitud ,moda_lo, latitud, moda_la, HMA,moda_ho, total rooms,moda_Tr, total bedrooms,moda_Tb, población,moda_P, house holds,moda_hh , media income, moda_mi,  MHV, moda_mh, oceanproximity,moda_op  )
#print (la mediana de los valores es: , mediana )
#print (la desviación estandar de los valores es: , DS)

#print("Moda de 'longitude':", moda_longitude)
#print("Moda de 'latitude':", moda_latitude)
#print("Moda de 'housing_median_age':", moda_housing_median_age)

#sub = df.iloc[[9]] #lo mismo que el de abajo
#print(df [9:10] ) #lo mismo pero con selección de renglones indirecto

#print(df['age'][0:1]) #sirve para imprimir una de una secsión solo los renglones 0 y 1, en este caso de age. 
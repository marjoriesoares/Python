 #Trabajo con datos reales - CSV
 #link: https://data.buenosaires.gob.ar/dataset/

from google.colab import drive
import pandas as pd
import numpy as np
variableTurnos = pd.read_csv(ruta+ "/dataset_turnos_detalle.csv")
variableTurnos.sample(3)
variableTurnos['fecha_cita'].value_counts()


import json

data_content= str(variableTurnos['fecha_cita'].value_counts())
data= open(ruta + '/myfirstJson.json', 'w')
data.write(data_content)
data.close()
#1. Mi Mascota

# Crea un programa que pida por teclado (input) 
# los datos de tu mascota y 
#los mismos se guarden en un 
# archivo que se llame miMascota.txt.

from google.colab import drive
drive.mount('/drive')

ruta = '/drive/MyDrive/Colab Notebooks'

nombre=input('Cual es el nombre de tu mascota? ')
apellido=input('Cual es el apellido de tu mascota? ')
idad=input('Cual es la idad de tu mascota? ')
d= {'NOMBRE':nombre,'APELLIDO':apellido,'IDAD':idad}
f = open(ruta + "/miMascota3.txt", "w")

f.write(d['NOMBRE']+'\n'+ d['APELLIDO']+'\n'+str(d['IDAD']))

f.close()


#2. Archivos JSON - Escritura

import json
firstname=input('What is your firstname? ')
lastname=input('What is your lastname? ')
age=input('How old are you? ')
amount=input('How much do you earn in a month? ')

data={}
data['clients']=[]
data['clients'].append({
    'firstname': firstname,
    'lastname':lastname,
    'age':age,
    'amount':amount})
with open(ruta + '/myfirstJson.json', 'w') as file:
  json.dump(data, file, indent=4)


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
#Mi Mascota

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

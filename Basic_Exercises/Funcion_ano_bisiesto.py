# Funcion año bisiesto 
#a.Recibirá un año por parámetro
#b.Imprimirá “El año año es bisiesto” si el año es bisiesto
#c.Imprimirá “El año año no es bisiesto” si el año no es bisiesto
#d.Si se ingresa algo que no sea número debe indicar que se ingrese un número.

def es_bisiesto(ano):
  if (type(ano) != int):
   print(f'"{ano}" no es un año. Ingrese un numero.')
  else:
   bisiesto= (ano%4==0) and (ano%100!=0) or (ano%400==0)
   if bisiesto is True:
    print(f'El año {ano} es bisiesto')
   elif bisiesto is False:
    print(f'El año {ano} no es bisiesto') 
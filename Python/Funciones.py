#Python Exercises Coder


#1 Funcion año bisiesto 
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

#2 Funcion par o impar
#a. Recibirá un número por parámetro
#b.Imprimirá Par si el número es par
#c. Imprimirá Impar si el número es impar
# d. Si se ingresa algo que no sea número debe indicar que se ingrese un número.

def par_o_impar(numero):
 if (type(numero)!=int):
   return ('No es un numero. Ingrese un numero: ')
 else:
   numero=int(numero)
   if (numero%2)==0:
    return (f'{numero} es par')
   else:
    return (f'{numero} es impar')  
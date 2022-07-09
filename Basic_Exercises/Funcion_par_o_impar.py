
#Funcion par o impar
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
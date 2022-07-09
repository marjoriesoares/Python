'''1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:


1.	Mostrar una suma de los dos números
2.	Mostrar una resta de los dos números (el primero menos el segundo)
3.	Mostrar una multiplicación de los dos números
4.	Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
5.	En caso de no introducir una opción válida, el programa informará de que no es correcta.
'''

num_1=input("Ingrese un numero: ")
while (not num_1.isnumeric()): #Fijando si el input es un numero
 num_1=input("No es numero. Ingrese un numero: ")
else:
  num_1=int(num_1)

num_2= input("Ingrese mas un numero: ")
while (not num_2.isnumeric()): #Fijando si el input es un numero
 num_2=input("No es numero. Ingrese un numero: ")
else:
 num_2=int(num_2)

operaccion=input("Cual operaccion? (Elige un numero de 1 a 4)\n1. Suma\n2. Resta\n3. Multiplicación\n4. Finalizar programa\n")


while (not operaccion.isnumeric()): #Fijando si el input para selecion de las operaciones es un numero
 print("Esta entrada no es valida. Intentalo otra ves.")
 operaccion=input("Cual operaccion? (Elige un numero de 1 a 4)\n1. Suma\n2. Resta\n3. Multiplicación\n4. Finalizar programa\n")
else:
 operaccion=int(operaccion)
#Operaciones selecionadas
if operaccion==1: 
 resultado=str(num_1+num_2)
 print("Resultado: "+str(num_1)+"+"+str(num_2)+"="+resultado)
elif operaccion==2:
 resultado=str(num_1-num_2)
 print("Resultado: "+str(num_1)+"-"+str(num_2)+"="+resultado)
         
elif operaccion==3:
 resultado=str(num_1*num_2)
 print("Resultado: "+str(num_1)+"*"+str(num_2)+"="+resultado)
elif operaccion==4: 
  print("Programa finalizado!")
elif operaccion>4 and operaccion<=0:  #Fijando si el input para selecion es valido(entre 1 e cuatro)
 while (operaccion>4):
  print("Esta entrada no es valida. Intentalo otra ves.")
  operaccion=input("Cual operaccion? (Elige un numero de 1 a 4)\n1. Suma\n2. Resta\n3. Multiplicación\n4. Finalizar programa\n")
      #Testea si el nuevo input es numerico
  while (not operaccion.isnumeric()):
   print("Esta entrada no es valida. Intentalo otra ves.")
   operaccion=input("Cual operaccion? (Elige un numero de 1 a 4)\n1. Suma\n2. Resta\n3. Multiplicación\n4. Finalizar programa\n")
  else:
   operaccion=int(operaccion)

else:
  print("Programa finalizado!")
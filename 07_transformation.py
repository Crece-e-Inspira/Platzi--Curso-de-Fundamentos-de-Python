'''
Python tiene variable dinamicas, depende del dato que ingresemos, Python automaticamente
cambiara el tipo de variable.

'''
import string

name = "Jhordan" #Tipo de datos 'str', texto
name = 12        #Tipo de dato 'int', entero
name = "12"      #Tipo de dato 'str', texto
name = True      #Tipo de dato 'boolean', booleano

#----------------------------------------------------------------
'''
Al escribir un valor de entrada se guarda como dato tipo 'str',
como lo queremos a tipo numero lo convertimos.

Lo pasamos dentro de la funcion 'int()' para convertirlo a entero.
En caso de el numero tenga decimales se utiliza float(), para convertir a numero decimal. 
'''
edad = input("Escribe tu edad: ")                       #Tipo de dato 'str'
print( type(edad))

edad = int( input("Escribe tu edad: "))                 #Convierte a tipo de dato 'int', entero
print( type(edad))

estatura = float( input("De cuanto es tu estatura: "))  #Convierte a tipo de dato 'float', entero decimal
print( type(estatura))


#----------------------------------------------------------------
'''
APORTE
Para declara una variable constante:
'''
user: str = "JhordynEc20"
age: int = 19
es_estudiante: bool = True

#----------------------------------------------------------------
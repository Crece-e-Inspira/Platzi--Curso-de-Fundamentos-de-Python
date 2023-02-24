#Concatenacion
'''
La concatenacion es unir valores de otras variables en uno
solo.
'''

name = "Jhordan"
last_name = "P. Bustamat"

# 1. Primera forma de concatenar
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print("V1", template)


# 2. Segunda forma de concatenar
'''
los simbolos {}, se remplazaran por lo que tenga format.()
Es decir se remplazaran en orden:

"Hola, mi nombre es {1} y mi apellido es {2}".format(name~1, last_name~2)
'''

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print("V2", template)


#3. Tercera forma de concatenar
'''
Similar a la segunda forma de concatenar pero incrustado en el texto.
Todo lo que este dentro del simbolo {aqui!} sera tratado como una variable incrustada
y no como un texto normal.
'''
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print("V3", template)


'''
Si bien el resultado es el mismo, al nivel de codigo es distinto.
La tercera forma de concatenar es el mas utilizado, por que tiene una estructura mas entendible.
'''
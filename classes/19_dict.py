#Diccionario
my_dict = {}

print(type(my_dict))

my_dict = {
    'avion': 'definicion',
    'name': 'Jhord',
    'last_name': 'piz',
    'age': 19
}

print(my_dict)

#Contar elementos del diciconario
print(len(my_dict))

#Imprimir valor de llave
print(my_dict['name'])

#Si no existe un elemento nos devuelve, NONE y no error
print(my_dict.get('age'))

#Validad el elemento en la lista
print('avion' in my_dict)
print('avioness' in my_dict)

# [ ] = Listas
# ( ) = Tuplas
# { } = Diccionario
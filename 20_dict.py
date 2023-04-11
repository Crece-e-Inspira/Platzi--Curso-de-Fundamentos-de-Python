person = {
    'name': 'Jhord',
    'last_name': 'Piz',
    'language': ['Python', 'Javascript'],
    'age': 19
}

print(person)

# Cambiar valores en los diccionarios
person['name'] = 'Jhair'
person['age'] -= 2
#
person['language'].append('rust')

print(person)

#Eliminar atributo del diccionario
del person['last_name']
person.pop('age')

print(person)

#Imprimir elementos
print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())
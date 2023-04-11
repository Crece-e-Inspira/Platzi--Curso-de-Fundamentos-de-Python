#for
'''
for element in range(1, 21):
    print(element)
'''

#Recorriendo la lista con for
my_list = [43, 45, 67, 89, 43]
for element in my_list:
    print(element)

#Recoriendo la tupla con for
my_tuple = ('nico', 'julian', 'Jhord')
for element in my_tuple:
    print(element)

#Recorre el diccionario con for
product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}

for key in product:
    print(element, product[key])

#Otra manera de hacer lo mismo
for key, value in product.items():
    print(key, ' => ', value)

#Lista con diccionario
:wq:

for person in people:
    print(person)
    print('name --> ', person['name'])

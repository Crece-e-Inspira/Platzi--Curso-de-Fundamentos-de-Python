#tupla, solo se declara no se puede eliminar. Como una constate.
#lectura y leer
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(numbers), numbers)

string =("nico", "zule", "santy")
print(type(string), string)

print("0 ==> ", numbers[0])

#Buscar la posicion
print("Buscar la posicion", string.index('zule'))

#Contar cuantas veces esta el elemento en la tupla
print(string.count('nico'))

#Para convertirlo a un lista. tupla a lista
my_list = list(string)
print(type(my_list), my_list)

#De lista a tupla
my_tupla = tuple(my_list)
print(type(my_tupla), my_tupla)
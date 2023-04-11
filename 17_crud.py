#CRUD Create, read, update & delete

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(number[1])

number[-1] = 10
print(number)

#Agregar un nuevo elemento
number.append(7000)
print(number)

#Agregar nuevo elemento por posicion
number.insert(0, "Hola")
print(number)

task = ["todo 1", "todo 2", "todo 3", "todo 4"]

#fusionar lista
new_list = number + task
print(new_list)

#para preguntar la posicion del elemento
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

#Eliminar un elemento de la lista
new_list.remove("todo 1")
print(new_list)

#Elimina el ultimo elemento de la lista
new_list.pop()
print(new_list)

#Pop tambien elimina por el numero de posicion
new_list.pop(0)
print(new_list)


#Voltear el array
new_list.reverse()
print(new_list)

#Ordenar el elemento de la lista
number_a = [1, 4, 5, 3]
number_a.sort()
print(number_a)

#Cuando hay tipos de datos mesclados .sort no va a funcionar
string = ["re", "a", "z", "b", "ga"]
string.sort()
print(string)
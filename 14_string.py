text = "Ella sabe programar en Python"
print("JavaScript" in text)
print("Python" in text)

if 'Python' in text:
    print('Si esta')
else:
    print('No esta')

size = len(text)
print(size)

print(text)

#Convierte el texto a mayuscula
print(text.upper())

#Convierte el texto a minuscula
print(text.lower())

#Cuenta cuantos de esa letra hay.
print(text.count('a'))


#Invierte lo mayuscula a minuscula y viseversa
print(text.swapcase())


#Verific si el texto comienza por esa parala
print(text.start('Ella'))

#lo contrario del anterior, termina en en esa palabra
print(text.endswith('rUST'))

#Renplaza el texto
print(text.replace("Python", "Go"))

text_2 = "Este es un titulo"
print(text_2)

#Pone el primer caracter en Mayuscula
print(text.capitalize())

#Pone el inicio de cada palabra en mayuscula
print(text_2.title())

#Verific si el texto es un dujito(numero)
print(text_2.isdigit())
print("398".isdigit())

#!!!!!!!!Mas informacion sobre metodos string
info = "https://www.w3schools.com/python/python_strings_methods.asp"
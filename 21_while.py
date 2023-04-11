#El WHILE Similar a esta sintaxis
if True:
    print('Se ejecuta')

#while
'''
while True:
    print('While se ejecuta')


contador = 0
while contador < 10:
    contador += 1
    print(contador)


contador = 0

while contador < 20:
    contador += 1
    if contador == 15:
        # BREAK es una forma forzada de romper el ciclo
        break
    print(contador)
'''

contador = 0
while contador < 20:
    contador += 1
    if contador < 15:
        #Salta a la siguiente iteracion obviando los codigos siguientes
        continue
    print(contador)
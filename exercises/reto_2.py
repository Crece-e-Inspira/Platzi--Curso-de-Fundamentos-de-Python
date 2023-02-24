# Juego, piedra papel o tijera
import random as rd

mensj = '''
Elige una opcion:
'1' Papel
'2' Tijera
'3' Piedra
USER🧑👋 >>> '''

# Entrada de usuario y verificar si esta en el rango de opciones con el tipo de datos
user_number = int( input(mensj))
if not (user_number >= 1 and user_number <= 3):
    print("Opcion Invalida")
    exit()

# Entrada de PC
pc_number = rd.randint(1, 3)
print("PC💻👋 >>>", pc_number)

#Numeros distintos hay un ganardor, numeros iguales empate
if user_number != pc_number:
    # Papel o tijera, el numero menor gana
    if (user_number == 3 and pc_number == 1) or not (user_number == 3 and pc_number == 1):
        if user_number < pc_number:
            print("Gana TU!")
        else:
            print("Gana PC!")

    elif user_number < pc_number:
        print("Gana PC!")
    else:
        print("Gana TU!")
else:
    print("Es un Empate!")
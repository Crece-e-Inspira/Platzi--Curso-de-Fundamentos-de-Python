import random as rd

from bs4 import element

elements = ('papel', 'Piedra', 'Tijera')

mensaje = '''
Elige una opcion

Papel --> 0
Piedra  --> 1
Tijera --> 2

: '''
user_option = int(input(mensaje))
pc_option = rd.randint(0, 2)


#Papel --> Piedra
if user_option == 0 and pc_option == 1:
    print('Gana Usuario!!!')
    print(f'Eligiste ***{elements[user_option]}***,  Pc elige *{elements[pc_option]}*')

#Piedra --> Tijera
elif user_option == 1 and pc_option == 2:
    print('Gana Usuario!!!')
    print(f'Eligiste ***{elements[user_option]}***,  Pc elige *{elements[pc_option]}*')

#Tijera --> Papel
elif user_option == 2 and pc_option == 0:
    print('Gana Usuario!!!')
    print(f'Eligiste ***{elements[user_option]}***,  Pc elige *{elements[pc_option]}*')
#Pierde
else:
    print('Pierde** Usuario!!!')
    print(f'Eligiste ***{elements[user_option]}***,  Pc elige *{elements[pc_option]}*')



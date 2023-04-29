import string
import random


'''
JUEGO DE PIEDRA, PAPEL O TIJERA

-JUGADOR
-RONDAS
'''

'''
def verify_username(user):
    check_limit: bool = False
    check_characters: bool = False

    character_limit: int = 15

    user_name: str = '@{}'.format(user.title())
    user_name: str = user.replace(' ', '')

    supported_characters: str = '{}{}{}'.format(string.ascii_letters, '-_.', string.digits)

    # Verifica limites de caracteres
    if len(user_name) <= character_limit:
        check_limit: bool = True

    # Verifica si tiene caracteres permitidos
    if check_limit is True:
        i: int = 0
        for character in user:
            if character in supported_characters:
                i += 1
                if i == len(user_name):
                    check_characters: bool = True
            else:
                break

    valid_username: bool = character_limit and check_characters

    return valid_username
    #----------------------------------------------------------------

username_attempts = 3

while True:
    username = input('TU NOMBRE DE USUARIO🧐>>> @')

    if verify_username(username) is False:
        username_attempts -= 1
        if username_attempts == 0:
            exit()

        print('Ingrese un username valido')
        continue
    break
'''

def analyze_user_option(option):
    option = option.replace(' ', '')


    defined_option: None = None
    element: None = None

    #opcion por numero
    if option.isdigit():
        if len(option) == 1:
            element: int = int(option)
            if element > 0 and element <= 3:
                defined_option: int = element - 1

        else:
            return defined_option

    #*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
    #Opcion por texto
    element: string = option.lower()

    character_limit: int = 6
    game_elements: tuple = ['tijera', 'papel', 'piedra']

    print(len(element))

    if len(element) > character_limit or not(element.isalpha):
        print('h')
        return defined_option

    if element in game_elements:
        if element == 'tijera':
            defined_option: int = 0
        elif element == 'papel':
            defined_option: int = 1
        elif element == 'piedra':
            defined_option: int = 2

    return defined_option

message_user_options = '''
Escribe el numero o el nombre del elemento 'español'
~ 1 >> Tijera✂️
~ 2 >> Papel📄
~ 3 >> Piedra🪨
Elige >>> '''

while True:
    elements = ('Tijera✂️', 'Papel📄', 'Piedra🪨')

    pc_option = random.randint(1, 3)
    print(pc_option)

    user_option = input(message_user_options)
    user_option = analyze_user_option(user_option)


    print(elements[user_option])

    #rint(elements)
    exit()
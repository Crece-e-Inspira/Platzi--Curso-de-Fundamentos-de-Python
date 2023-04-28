import string

'''
JUEGO DE PIEDRA, PAPEL O TIJERA

-JUGADOR
-RONDAS
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
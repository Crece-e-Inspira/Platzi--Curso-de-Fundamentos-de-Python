import string
import random

def verify_username(user):
    check_limit: bool = False
    check_characters: bool = False

    character_limit: int = 15

    user_name: str = '@{}'.format(user.title())
    user_name: str = user_name.replace(' ', '')

    supported_characters: str = '{}{}{}'.format( string.ascii_letters, '@-_.', string.digits)

    # Verifica limites de caracteres
    if (len(user_name) <= character_limit) and (user != ''):
        check_limit: bool = True

    # Verifica si tiene caracteres permitidos
    if check_limit is True:
        i: int = 0
        for character in user_name:
            if character in supported_characters:
                i += 1
                if i == len(user_name):
                    check_characters: bool = True
            else:
                break

    valid_username: bool = check_limit and check_characters

    return valid_username, user_name
    #----------------------------------------------------------------

def analyze_user_option(option):
    option = option.replace(' ', '')

    defined_option: bool = False
    element: None = None

    #opcion por numero
    if option.isdigit():
        if len(option) == 1:
            element: int = int(option)
            if element > 0 and element <= 3:
                defined_option: int = element - 1
            else:
                return defined_option
        else:
            return defined_option

    #*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

    #Opcion por texto
    element: string = option.lower()

    character_limit: int = 6
    game_elements: tuple = ['tijera', 'papel', 'piedra']

    if len(element) > character_limit or not(element.isalpha):
        return defined_option

    if element in game_elements:
        if element == 'tijera':
            defined_option: int = 0
        elif element == 'papel':
            defined_option: int = 1
        elif element == 'piedra':
            defined_option: int = 2

    return defined_option

def verify_gameround(user_num):
    num: str = user_num.replace(' ', '')

    if num.isdigit():
        num: str = num
    else:
        num: bool = False

    return num

def the_winner_is(win, user, user_element, pc, pc_element):

    if win is True:
        the_winner: str = '{} GANADOR!!!\n{} >>|{} VS {}|<< {}'.format(user, user, user_element, pc_element, pc)
    elif win is False:
        the_winner: str = '{} GANADOR!!!\n{} >>|{} VS {}|<< {}'.format(pc, pc, pc_element, user_element, user)
    elif win is None:
        the_winner: str = 'EMPATES!!!\n{} >>|{} VS {}|<< {}'.format(pc, pc_element, user_element, user)
    else:
        the_winner: None = None

    return the_winner



message_user_options = '''{}
    Escribe la opción o el nombre del elemento
    OPCION : ELEMENTO
    ~  1  >>  TIJERA
    ~  2  >>  PAPEL
    ~  3  >>  PIEDRA
       
Elige >>> '''.format('*'*65)

message_user_options_2 = 'Elige >>> '

failed_attempts_allowed = 3

while True:
    username = input('Username >>> @')
    username = verify_username(username)

    if username[0] is False:
        failed_attempts_allowed -= 1
        if failed_attempts_allowed == 0:
            exit()
        print('Ingrese un username valido')
        continue

    game_round = input('Rondas: ')
    if isinstance(verify_gameround(game_round), str):
        game_round = int(verify_gameround(game_round))
        break
    else:
        game_round = 1
        print('Invalido. Automatico {} Ronda'.format(game_round))
        break

elements = ('TIJERA', 'PAPEL', 'PIEDRA')
rounds_allowed_ruling = 3
round = 0
playable_rounds = game_round
pc_username = '@The_pc404'
user_gains = 0
pc_gains = 0


while True:

    pc_option = random.randint(0, 2)

    if round == 0:
        user_option = input(message_user_options)
    else:
        user_option = input(message_user_options_2)

    user_option = analyze_user_option(user_option)

    if user_option is False:
        rounds_allowed_ruling -= 1
        print('Opcion Invalida.')
        if rounds_allowed_ruling <= 0:
            break
        continue


    round += 1
    winner = '{}\nRONDA ({} de {}) {}\n{}'.format('~-' * 21,round,playable_rounds, the_winner_is(True, username[1], elements[user_option], pc_username, elements[pc_option]), '~-' * 21)

    # 0 TIJERA VS PAPEL 1
    if (user_option == 0) and (pc_option == 1):
        user_gains += 1
        print(winner)

    # 1 PAPEL VS PIEDRA  2
    elif (user_option == 1) and (pc_option == 2):
        user_gains += 1
        print(winner)

    # 2 PIEDRA VS TIJERA 1
    elif (user_option == 2) and (pc_option == 0):
        user_gains += 1
        print(winner)

    #Empates
    elif user_option == pc_option:
        print('{}\nRONDA ({} de {}) {}\n{}'.format('~-' * 21,round,playable_rounds, the_winner_is(None, username[1], elements[user_option], pc_username, elements[pc_option]), '~-' * 21))

    else:
        pc_gains += 1
        print('{}\nRONDA ({} de {}) {}\n{}'.format('~-' * 21,round,playable_rounds, the_winner_is(False, username[1], elements[user_option], pc_username, elements[pc_option]), '~-' * 21))


    game_round = game_round - 1
    if game_round == 0:
        if user_gains > pc_gains:
            print('{} ES EL GANADOR!'.format(username[1]))
        elif user_gains < pc_gains:
            print('{} ES EL GANADOR!'.format(pc_username))
        else:
            print('NO HAY GANADORES, EMPATES!!')
        exit()
from time import sleep
def sistemaajuda():
    comando = ' '
    while comando != 'fim':
        sleep(0.5)
        print('\033[30:42m', end = '')
        print('~' * 23)
        print('SISTEMA DE AJUDA PyHELP')
        print('~' * 23)
        print('\033[m', end='')
        comando = input('Digite o comando ou Função ou Biblioteca > ')
        if comando == 'fim':
            print('\033[30:41m', end='')
            print('~' * 10)
            print('Até Logo!')
            print('~' * 10)
        else:
            print('\033[30:44m', end = '')
            print('~' * 35)
            print(f'Acessando o manual do comando {comando}')
            print('~' * 35)
            sleep(1)
            print('\033[37:40m')
            help(comando)
sistemaajuda()
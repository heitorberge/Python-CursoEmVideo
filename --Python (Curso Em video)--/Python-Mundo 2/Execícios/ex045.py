from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)
print('Suas opções:')
print('[ 0 ]Pedra')
print('[ 1 ]Papel')
print('[ 2 ]Tesoura')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('-=' * 15)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
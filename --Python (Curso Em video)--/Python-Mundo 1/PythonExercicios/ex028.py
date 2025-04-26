from random import randint
from time import sleep
computador = randint(0,5)
print('-=-' * 25)
print('        Eu pensei em um número entre 0 e 5,Tente Adivinhar...')
print('-=-' * 25)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if computador == jogador:
    print('PARABÉNS! Você adivinhou o número que eu pensei!')
else:
    print('GANHEI!Eu pensei no número {} não no número {}'.format(computador,jogador))
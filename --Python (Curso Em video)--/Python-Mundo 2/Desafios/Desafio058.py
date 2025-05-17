from random import randint
print('Eu pensei em um número entre 0 e 10,Tente Adivinhar...')
com = randint(0,10)
jogador = -2
p = 1
while com != jogador:
    jogador = int(input('Em que número eu pensei? '))
    if com == jogador:
        print('PARABÉNS! Você adivinhou o número que eu pensei!')
    else:
        print('GANHEI!')
        print('Tente Novamente...')
        p+=1
print('Você precisou de {} palpites para acertar o número que pensei.'.format(p))
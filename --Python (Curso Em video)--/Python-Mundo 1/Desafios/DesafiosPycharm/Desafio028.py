import random
print('-- ADIVINHE SEU NÚMERO--')
us = input('Digite seu nome de usuario: ')
print('Carregando...')
ns = random.randint(1, 5)
print('Eu pensei em um número entre 1 e 5, Que número é este, {}?'.format(us))
palp = int(input('De seu Palpite: '))
if palp == ns:
    print('Você leu minha Mente, Você ganhou, pois o número sorteado era {}!'.format(ns))
else:
    print('Sinto muito, {}, Você perdeu, pois número sorteado era {}.'.format(us,ns))
print('Deseja jogar denovo?Se sim aperte o Botão de play ▶.')
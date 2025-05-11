import random
print('Vamos Jogar Pedra Papel Tesoura?')
ppt = ['Pedra', 'Papel', 'Tesoura']
s = random.choice(ppt)
print('Você vai Jogar...')
print('1-Pedra')
print('2-Papel')
print('3-Tesoura')
res = int(input(''))
if (res == 1 and s == 'Papel') or (res == 2 and s == 'Tesoura') or (res == 3 and s == 'Pedra'):
    print('Ganhei! Pois eu Joguei {}'.format(s))
elif (res == 1 and s == 'Tesoura') or (res == 2 and s == 'Pedra') or (res == 3 and s == 'Papel'):
    print('Perdi! Pois eu Joguei {}'.format(s))
elif res == 1 and s == 'Pedra' or res == 2 and s == 'Papel' or res == 3 and s == 'Tesoura':
    print('Empate! Pois eu Joguei {} e você também!'.format(s))
else:
    print('Número Inválido, Digite 1, 2 ou 3.')
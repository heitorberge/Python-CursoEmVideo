import datetime

aa = datetime.datetime.now().year
while True:
    anasc = int(input('Em que ano você nasceu? '))
    if anasc >= 1908:
        break
    else:
        print('Por favor, digite um ano de nascimento igual ou posterior a 1908.')

idade = aa - anasc
if idade < 18:
    print('Você ainda vai se alistar no exército.')
    tempo = 18 - idade
    print('Falta {} anos para você se alistar!'.format(tempo))
elif idade == 18:
    print('Está na hora de se alistar no exército!')
else:
    print('Já passou o tempo de alistamento!')
    tempo = idade - 18
    print('Já passaram {} anos do prazo.'.format(tempo))
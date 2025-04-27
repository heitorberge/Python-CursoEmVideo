import datetime
aa = datetime.datetime.now().year
anasc = int(input('Em que ano você nasceu? '))
idade = aa-anasc
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
import datetime
atual = datetime.datetime.now().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual-nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Está na hora de se alistar no exército!')
elif idade < 18:
    print('Você ainda vai se alistar no exército.')
    tempo = 18 - idade
    print('Falta {} anos para você se alistar!'.format(tempo))
    ano = atual + tempo
    print('Seu alistamento será em {}'.format(ano))
else:
    print('Já passou o tempo de alistamento!')
    tempo = idade - 18
    print('Já passaram {} anos do seu alistamento.'.format(tempo))
    ano = atual - tempo
    print('Seu alistamento foi em {}'.format(ano))
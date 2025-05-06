import datetime
aa = datetime.datetime.now().year
nasc = int(input('Em que ano você nasceu? '))
i = aa - nasc
print('O atleta tem {} anos'.format(i))
if i <= 9:
    print('Classificação: MIRIM')
elif i <= 14:
    print('Classificação: INFANTIL')
elif i <= 19:
    print('Classificação: JUNIOR')
elif i <= 25:
    print('Classificação: SÊNIOR')
elif i > 25:
    print('Classificação: MASTER')
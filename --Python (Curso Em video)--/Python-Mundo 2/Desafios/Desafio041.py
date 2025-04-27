import datetime
aa = datetime.datetime.now().year
print('--- Confederação Nacional de Natação ---')
nasc = int(input('Em que ano você nasceu? '))
i = aa - nasc
if i < 9:
    print('Você é um nadador MIRIM')
elif 9 < i < 14:
    print('Você é um nadador INFANTIL')
elif 14 < i < 19:
    print('Você é um nadador JUNIOR')
elif 19 < i <= 20:
    print('Você é um nadador SÊNIOR')
elif i > 20:
    print('Você é um nadador MASTER')
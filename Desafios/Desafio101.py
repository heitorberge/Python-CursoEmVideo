from datetime import date
def voto(anasc):
    idade = date.today().year - anasc
    if idade >= 16 and idade < 18:
        return 'Opcional'
    elif idade >= 18 and idade < 65:
        return 'Obrigatório'
    else:
        return 'Negado'


print('-'*30)
nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - nasc
print(f'Com {idade} anos o seu voto é {voto(nasc)}')
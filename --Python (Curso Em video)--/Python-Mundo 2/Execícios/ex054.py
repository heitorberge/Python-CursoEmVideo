import datetime
tma = 0
tme = 0
for c in range(1,8):
    anasc = int(input('Em que ano a {}ª pessoa nasceu?  '.format(c)))
    idade = datetime.datetime.now().year - anasc
    if idade >=  21:
        tma+=1
    else:
        tme+=1
print('{} Pessoas Atingiram a Maior Idade'.format(tma))
print('{} Pessoas Não Atingiram a Maior Idade'.format(tme))
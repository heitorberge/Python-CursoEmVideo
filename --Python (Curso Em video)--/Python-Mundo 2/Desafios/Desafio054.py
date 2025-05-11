import datetime
s1 = 0
s2 = 0
for c in range(0,7):
    anasc = int(input('Digite um ano de nascimento: '))
    idade = datetime.datetime.now().year - anasc
    if idade >=  18:
        s1+=1
    else:
        s2+=1
print('{} Pessoas Atingiram a Maior Idade'.format(s1))
print('{} Pessoas Não Atingiram a Maior Idade'.format(s2))
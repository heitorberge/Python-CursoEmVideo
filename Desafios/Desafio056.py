mi = 0
mm = 0
maior = 0
for c in range(1,5):
    nome = str(input('Nome da {}° Pessoa: '.format(c)))
    idade = int(input('Idade da {}° Pessoa: '.format(c)))
    sexo = str(input('Sexo da {}° Pessoa (M/F): '.format(c))).upper()
    mi += idade
    if idade > maior and sexo == 'M':
        mn = nome
    if sexo == 'M' and idade < 20:
        mm += 1
mi = int(mi / 4)
print('A média de idade dessas pessoas é {}'.format(mi))
print('O nome do homem mais velho é {}'.format(mn))
print('{} Mulheres tem menos de 20 anos'.format(mm))
print('-=-' * 5)
print('Gerador de PA')
print('-=-' * 5)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} →'.format(termo), end = ' ')
    termo += razão
    cont += 1
print('FIM')
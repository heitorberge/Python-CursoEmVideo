primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razao
for c in range(primeiro,décimo + 1,razao):
    print('{}'.format(c), end = ' → ')
print('Fim')
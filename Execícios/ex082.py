num = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer Continuar? [S/N] '))
    if resp in 'Nn':
        break
print(num)
pares = list()
impares = list()
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
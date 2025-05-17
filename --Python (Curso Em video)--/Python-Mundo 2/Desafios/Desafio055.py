maior = 0
menor = float('inf')
for c in range(0,5):
    peso = float(input('Digite o peso de uma pessoa: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('A pessoa mais pesada tinha {:.1f}Kg e a mais leve tinha {:.1f}Kg'.format(maior,menor))
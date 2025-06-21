import moeda3
p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda3.moeda(p)} é {moeda3.metade(p, format=True)}')
print(f'O dobro de {moeda3.moeda(p)} é {moeda3.dobro(p, format=True)}')
print(f'Aumentando 10%, temos {moeda3.aumentar(p, 10, format=True)}')
print(f'Diminuindo 13%, temos {moeda3.diminuir(p, 13, format=True)}')

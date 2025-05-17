soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print('A soma dos números impares entre 1 e 500 que são multiplos por 3 é {}'.format(soma))
print('FIM')
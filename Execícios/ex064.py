núm = cont = soma = 0
while núm != 999:
    núm = int(input('Digite um número [999 para parar]: '))
    soma += núm
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont - 1, soma - 999))
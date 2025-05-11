n = 0
s = 0
c = 0
while n != 999:
    n = int(input('Digite um valor: '))
    if n == 999:
        s = s
    else:
        s += n
        c += 1
print('{} Números Digitados.'.format(c))
print('A soma de todos os números é {}.'.format(s))
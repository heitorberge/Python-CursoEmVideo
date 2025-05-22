n = int(input('Digite um valor: '))
a, b = 0, 1
sequencia = []
while a < n:
    sequencia.append(a)
    a, b = b, a + b
print('{}'.format(sequencia))
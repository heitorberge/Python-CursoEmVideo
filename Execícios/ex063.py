print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
cont = 0
t1 = 0
t2 = 1
print('~~' * n * 4)
if n >= 1:
    print('{} → '.format(t1), end='')
    cont += 1
if n >= 2:
    print('{} → '.format(t2), end='')
    cont += 1
while cont < n:
    t3 = t1 + t2
    print('{} → '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('~~' * n * 4)
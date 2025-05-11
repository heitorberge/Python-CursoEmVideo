from time import sleep
n = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(n, f + 1, p):
    print(c)
    sleep(1)
print('Fim')
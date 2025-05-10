s = 0
co = 0
for c in range(0,6):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0:
        s+=n
        co+=1
print('A soma de todos os {} valores pares digitados é {}'.format(co,s))
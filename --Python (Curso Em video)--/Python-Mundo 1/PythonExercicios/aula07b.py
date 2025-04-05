n1 = int(input('Um Valor: '))
n2: int = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
sub = n1 - n2
print('A soma é {} \nA multiplicação é {} \nA divisão é {:.3f} \nA subtração é {}'.format(s, m, d, sub))
print('A divisão inteira é {} \nA Potência é {}'.format(di, e))

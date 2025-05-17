print('--- Maior, Menor ou Igual? ---')
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
if n1 > n2:
    print('O número {} é maior que {}.'.format(n1,n2))
elif n2 > n1:
    print('O número {} é maior que {}.'.format(n2,n1))
else:
    print('Não existe valor maior, os dois são iguais.')
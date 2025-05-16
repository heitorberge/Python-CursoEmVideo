num = int(input('Digite um número Inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    binario = bin(num)[2:]
    print('{} convertido para BINÁRIO é igual a {}'.format(num, binario))
elif opção == 2:
    octal = oct(num)[2:]
    print('{} convertido para OCTAL é igual a {}'.format(num, octal))
elif opção == 3:
    hexadecimal = hex(num)[2:]
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hexadecimal))
else:
    print('Digite uma opção válida.')
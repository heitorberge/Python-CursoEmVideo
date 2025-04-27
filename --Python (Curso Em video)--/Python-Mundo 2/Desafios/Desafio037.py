num = int(input('Digite um número: '))
print('Você quer converter este número para...')
print('Digite 1 para binário')
print('Digite 2 para octal')
print('Digite 3 para hexadecimal.')
res = int(input(''))
if res == 1:
    num_convertido = bin(num)
    print(f'O número {num} em BINÁRIO é {num_convertido}')
elif res == 2:
    num_convertido = oct(num)
    print(f'O número {num} em OCTAL é {num_convertido}')
elif res == 3:
    num_convertido = hex(num)
    print(f'O número {num} em HEXADECIMAL é {num_convertido}')
else:
    print('Opção inválida. Por favor, digite 1, 2 ou 3.')
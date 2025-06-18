def leiaInt(Pergunta):
    n = input(Pergunta)
    if n.isnumeric():
        return int(n)
    else:
        print('\033[31mERRO! Digite um número inteiro válido.\033[0m')
        return leiaInt(Pergunta)


print('-' * 30)
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')
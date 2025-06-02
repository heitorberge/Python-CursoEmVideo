lista = list()
res = 'S'
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    res = input('Quer continuar? [S/N] ').strip().upper()[0]
    if res not in 'SN':
        print('Opção inválida! Tente novamente.')
        res = input('Quer continuar? [S/N] ').strip().upper()[0]
    if res == 'N':
        break
print('=-' * 30)
print(f'Você digitou os valores {sorted(lista)}')
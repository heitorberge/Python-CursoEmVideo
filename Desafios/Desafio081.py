lista = list()
res = 'S'
while res == 'S':
    lista.append(int(input('Digite um valor: ')))
    res = input('Quer continuar? [S/N] ').strip().upper()[0]
    while res not in 'SN':
        res = input('Resposta Inválida!Quer continuar? [S/N] ').strip().upper()[0]
print(f'Você digitou {len(lista)} números.')
print(f'A lista em ordem decrescente é: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')


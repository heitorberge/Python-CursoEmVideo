lista = list()
res = 'S'
while res == 'S':
    lista.append(int(input('Digite um valor: ')))
    res = input('Quer continuar? [S/N] ').strip().upper()[0]
    while res not in 'SN':
        res = input('Resposta Inválida!Quer continuar? [S/N] ').strip().upper()[0]
listapar = list()
listaimpar = list()
for n in lista:
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
print(f'Você digitou {lista}')
print(f'A lista de pares é: {listapar}')
print(f'A lista de ímpares é: {listaimpar}')
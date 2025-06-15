total = totmil = menor = cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    cont+= 1
    if cont == 1:
        menor = preco
        nome = produto
    else:
        if preco < menor:
            menor = preco
            nome = produto
    while preco < 0:
        print('Preço inválido! Tente novamente.')
        preco = float(input('Preço do produto: R$'))
    if preco > 1000:
        totmil += 1
    total += preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custa R${menor:.2f}')
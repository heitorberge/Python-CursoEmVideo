print('-' * 40)
print('         LOJA SUPER BARATÃO')
print('-' * 40)
c = 'S'
pt = 0
acm = 0
menor = 0
menornome = ''
cont = 0
while c == 'S':
    Np = str(input('Nome do produto: '))
    Pç = float(input('Preço : \033[92mR$\033[0m'))
    pt+=Pç
    cont += 1
    if Pç > 1000:
        acm += 1
    if cont == 1:
        menor = Pç
        menornome = Np
    elif Pç > menor:
        menor = Pç
        menornome = Np
    c = str(input('Deseja continuar? (S/N)')).upper().strip()[0]
print('---------------- Fim do progama ----------------')
print(f'O total da compra foi R${pt}')
print(f'Temos {acm} produtos custando mais que R$1000,00')
print(f'O produto mais barato foi a {menornome} que custa R${menor}')

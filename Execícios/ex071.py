print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
céd = 50
totlcéd = 0
while True:
    if total >= céd:
        total -= céd
        totlcéd += 1
    else:
        if totlcéd > 0:
            print(f'Total de {totlcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totlcéd = 0
        if total == 0:
            break
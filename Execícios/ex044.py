print('\033[96m{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('\033[94mPreço das compras: \033[92mR$'))
print('''\033[93mFORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no catão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('\033[94mQual é a opção?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print('\033[93mSua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('\033[93mSua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif opção == 3:
    total = preço
    parcela = total /  2
    print('\033[96mSua compra será parcelada em 2x de R${:.2f}'.format(parcela))
    print('\033[93mSua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('\033[94mQuantas parcelas? '))
    parcela = total /  totparc
    print('\033[96mSua compra será parcelada em {}x de R${:.2f}'.format(totparc,parcela))
    print('\033[93mSua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
else:
    total = preço
    print('\033[91mOPÇÃO INVÁLIDA DE PAGAMENTO.Tente Novamente')

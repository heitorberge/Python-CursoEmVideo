slr = float(input('Digite o salário de um funcionário: R$'))
aum = slr + (slr*15/100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(slr,aum))
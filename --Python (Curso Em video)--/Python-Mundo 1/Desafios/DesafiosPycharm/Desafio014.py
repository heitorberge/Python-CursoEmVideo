slr = float(input('Digite o salário de um funcionário: '))
prc = slr * 0.15
aum = slr + prc
print('O salário desta pessoa com 15% de aumento ficara: R${:.2f}'.format(aum))
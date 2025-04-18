slr = float(input('Digite o salário de um funcionário: '))
prc = 0
if slr > 1250:
    prc = slr * 0.10
else:
    prc = slr * 0.15
aum = slr + prc
print('O salário desta pessoa com aumento ficara: R${:.2f}'.format(aum))
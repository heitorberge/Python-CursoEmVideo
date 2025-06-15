slr = float(input('Digite o salário de um funcionário: R$'))
if slr <= 1250:
    novo = slr + (slr * 15 / 100)
else:
    novo = slr + (slr * 10 / 100)
print('Quem Ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(slr,novo))
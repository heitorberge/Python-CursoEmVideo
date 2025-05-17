print('----Banco do Elefante----')
print('Você vai comprar Uma Casa e precisa de um empréstimo?')
valorcasa = float(input('Qual o valor da Casa? R$'))
sal = float(input('Qual o valor do seu Salário? R$'))
anos = int(input('Em quantos anos Você vai pagar?'))
premen = anos * 12
pm = valorcasa / premen
print('O valor da prestação é R${:.2f} e você vai pagar em {} meses'.format(pm, premen))
if pm > sal * 0.30:
    print('Sinto muito mas a prestação do empréstimo é maior que 30% do seu salário.')
    print('Então não poderemos fazer o empréstimo.')
else:
    print('O empréstimo foi aprovado!')
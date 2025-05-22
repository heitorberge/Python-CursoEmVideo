km = float(input('Qual é a distância da sua viagem?: '))
print('Você está prestes a começar uma viagem de {:.1f}Km'.format(km))
pas = 0.0
if km <= 200:
    pas = km * 0.50
else:
    pas = km * 0.45
print('O preço da passagem será R${:.2f}'.format(pas))

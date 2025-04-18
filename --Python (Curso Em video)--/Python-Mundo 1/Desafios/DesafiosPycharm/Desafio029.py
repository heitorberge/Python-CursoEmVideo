km = int(input('Qual é a velocidade do seu carro em km/h? '))
multa = (km - 80) * 7
km2 = km-80
if km > 80:
    print('Você foi multado pois ultrapassou de 80km/h.')
    print('Contando que cada km/h a mais de 80 é R$7,00 de multa.')
    print('E o seu carro está {}km/h a mais que 80, Sua multa é de R${},00'.format(km2,multa))
else:
    print('Você não foi multado.')
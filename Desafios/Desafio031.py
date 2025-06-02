print('----RODÓVIARIA EM VÍDEO----')
km = float(input('Digite uma distancia de uma viagem em km que você ira fazer de ônibus: '))
pas = 0.0
if km <= 200:
    pas = km * 0.50
else:
    pas = km * 0.45
print('O preço da passagem será R${:.2f}'.format(pas))

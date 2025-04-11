lar = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = lar * alt
quant = area / 2
print('A área da parede é:  {} metros quadrados'.format(area))
print('A quantidade de tinta necessária para pintar a parede é:  {} litros'.format(quant))
def área(comprimento, largura):
    a = comprimento * largura
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m²')
print('-' * 20)
print('Controle de Terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(c, l)
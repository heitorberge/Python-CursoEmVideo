def escreva(msg):
    quant = len(msg) + 4
    print('~' * quant)
    print(f'{msg:^{quant}}')
    print('~' * quant)

# Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
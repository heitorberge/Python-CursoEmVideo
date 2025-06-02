lista = [[0, 0, 0] for _ in range(3)]
totpar = 0
tot3col = 0
mai2linha = 0
for c1 in range(0, 3):
    for c2 in range(0, 3):
        lista[c1][c2] = int(input(f'Digite um valor para a posição [{c1}, {c2}]: '))
        if lista[c1][c2] % 2 == 0:
            totpar += lista[c1][c2]
        if c2 == 2:
            tot3col += lista[c1][c2]
        if c1 == 1 and lista[c1][c2] > mai2linha:
            mai2linha = lista[c1][c2]
print
print(lista[0])
print(lista[1])
print(lista[2])
print('-=' * 30)
print(f'A soma dos valores pares é {totpar}.')
print(f'A soma dos valores da terceira coluna é {tot3col}.')    
print(f'O maior valor da segunda linha é {mai2linha}.')
# Fim do código
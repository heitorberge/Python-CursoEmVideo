lista = [[0, 0, 0] for _ in range(3)]
for c1 in range(0, 3):
    for c2 in range(0, 3):
        lista[c1][c2] = int(input(f'Digite um valor para a posição [{c1}, {c2}]: '))
print(lista[0])
print(lista[1])
print(lista[2])
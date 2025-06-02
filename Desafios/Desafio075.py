n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite outro número: '))
lista = (n1, n2, n3, n4)
vez9 = lista.count(9)
posição3 = lista.index(3) if 3 in lista else -1
contpares = 0
print(f'Você digitou os números: {lista}')
print(f'O número 9 apareceu {vez9} vezes')
if posição3 != -1:
    print(f'O número 3 apareceu pela primeira vez na {posição3 + 1}ª posição')
print(f'Os números pares digitados foram: ', end='')
for c in range(0,4):
    if lista[c] % 2 == 0:
        print(lista[c], end=' ')
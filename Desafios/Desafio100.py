from random import randint
def sorteia():
    lista = []
    for i in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Os números sorteados foram: {lista}')
    return lista
def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos números pares é: {soma}')
lista = sorteia()
somaPar(lista)
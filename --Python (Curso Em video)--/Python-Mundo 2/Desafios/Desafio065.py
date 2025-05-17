r = 'S'
menor = float('inf')
maior = 0
media = 0
cont = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    cont += 1
    media += n
    if n < menor:
        menor = n
    if n > maior:
        maior = n
    r = str(input('Deseja continuar? [S/N] '))
media = media / cont
print('A média dos números digitados é {}'.format(media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior,menor))

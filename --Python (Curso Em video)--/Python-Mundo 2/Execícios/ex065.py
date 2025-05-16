r = 'S'
soma = cont = media = maior = menor = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor == n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média dos números digitados é {}'.format(cont,media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior,menor))

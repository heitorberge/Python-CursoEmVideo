lista = []
mai = men = 0
while True:
    nome = input('Digite um nome: ')
    peso = float(input('Digite um peso: '))
    lista.append([nome, peso])
    if len(lista) == 1:
        mai = men = lista[0][1]
    else:
        if peso > mai:
            mai = peso
        if peso < men:
            men = peso
    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Resposta inválida!Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in lista:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {men}kg. Peso de ', end='')
for p in lista:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
 
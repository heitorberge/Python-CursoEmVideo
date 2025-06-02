lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c + 1}° valor: ')))
print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} e está nas posições: ', end='')
cont_maior = 0
for i, v in enumerate(lista):
    if v == max(lista):
        cont_maior += 1
        if cont_maior > 1:
            print('e ', end='')
        print(f'{i + 1} ', end='')
print()

print(f'O menor valor digitado foi {min(lista)} e está nas posições: ', end='')
cont_menor = 0
for i, v in enumerate(lista):
    if v == min(lista):
        cont_menor += 1
        if cont_menor > 1:
            print('e ', end='')
        print(f'{i + 1} ', end='')
print()
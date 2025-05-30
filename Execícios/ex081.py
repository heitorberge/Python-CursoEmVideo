valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente foram {sorted(valores, reverse=True)}')
print(f'O valor 5 {"faz parte" if 5 in valores else "não faz parte"} na lista.')
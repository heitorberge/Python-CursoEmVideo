listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90, 'Arroz', 19.90, 'Feijão', 7.50, 'Batata', 2.00, 'Cenoura', 1.50, 'Maçã', 5.00, 'Banana', 3.00, 'Laranja', 4.00, 'Uva', 6.00, 'Melancia', 8.00)
print('=-' * 20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=-' * 20)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:.<30} R${listagem[c + 1]:>7.2f}')
print('=-' * 20)
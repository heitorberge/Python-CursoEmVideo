from random import randint
from time import sleep
valoressorteados = {'Jogador 1': randint(1, 6),'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
print('Valores sorteados:')
for k, v in valoressorteados.items():
    print(f'    {k} tirou {v} no dado.')
    sleep(1)
print('Ranking dos jogadores:')
valoressorteados = sorted(valoressorteados.items(), key=lambda x: x[1], reverse=True)
for i, (jogador, valor) in enumerate(valoressorteados):
    print(f'    {i + 1}º lugar: {jogador} com {valor}.')
    sleep(1)
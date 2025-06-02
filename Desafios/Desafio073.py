times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino', 'Ceará', 'Bahia', 'Fluminense', 'Corinthians', 'Atlético-MG', 'Botafogo', 'São Paulo', 'Mirassol', 'Vasco', 'Fortaleza', 'Internacional', 'Vítoria', 'Grêmio', 'Juventude', 'Santos', 'Sport')
print('=-' * 20)
for c in range(0,6):
    print('Este time é um dos 5 primeiros colocados: ', times[c])
print('=-' * 20)
for c in range(16,20):
    print('Este time é um dos 4 últimos colocados: ', times[c])
print('=-' * 20)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('=-' * 20)
print(f'O time do Flamengo está na {times.index("Flamengo") + 1}º posição')
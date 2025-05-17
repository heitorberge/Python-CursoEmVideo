from time import sleep
print('Faltam 10 segundos pro estouro dos Fogos de artíficio!')
for c in range(10, 0 - 1, -1):
    print(c)
    sleep(1)
print('\033[91mEstouraram os fogos, EBA! 🎆')
print('Fim')
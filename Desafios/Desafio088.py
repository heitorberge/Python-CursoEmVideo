from random import randint
print('-=' * 30)
print('PALPITADOR DA MEGA SENA')
print('-=' * 30)
jogos = []
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
for _ in range(quantidade):
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogos.append(sorted(jogo))
print('-=' * 30)
for i, jogo in enumerate(jogos, start=1):
    print(f'Jogo {i}: {jogo}')
print('-=' * 30)
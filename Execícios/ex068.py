from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PIÍ':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end ='')
    print(' Deu PAR' if total % 2 == 0 else ' Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Ganhou')
            v += 1
        else:
            print('Você Perdeu')
            break
    elif tipo in 'IÍ':
        if total % 2 == 1:
            print('Você Ganhou')
            v += 1
        else:
            print('Você Perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes.')
from random import randint
print('-=-' * 10)
print('   VAMOS JOGAR PAR OU ÍMPAR?')
cont = 0
GouP = True
valor = 0
PoI = ''
soma = 0
while GouP:
    print('-=-' * 10)
    valor = int(input('Digite um valor: '))
    PoI = str((input('Par ou Ímpar? [P/I] '))).strip().upper()[0]
    valorc = randint(1,1000)
    print('---' * 10)
    soma = valorc + valor
    print(f'Você jogou {valor} e o computador {valorc}. No total deu {soma}, que é um número ', end='')
    if soma % 2 == 0:
        print('PAR')
        if PoI == 'P':
            print('Você venceu!')
            print('Vamos Jogar Novamente...')
            cont += 1
        else:
            print('Você perdeu!')
            Goup = False
            break
    else:
        print('ÍMPAR')
        if PoI == 'I':
            print('Você venceu!')
            print('Vamos Jogar Novamente...')
            cont += 1
        else:
            print('Você perdeu!')
            Goup = False
            break
print(f'Game Over! Você ganhou {cont} vezes.')
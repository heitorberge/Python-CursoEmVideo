from random import choice
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno azarado que vai ter que apagar o quadro é {}!'.format(escolhido))
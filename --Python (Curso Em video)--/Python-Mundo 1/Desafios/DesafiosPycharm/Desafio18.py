import random

print('O professor Jorel vai sortear um dos seus 4 alunos para apagar o quadro!')
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')
v = [a1, a2, a3, a4]
vs = random.choice(v)
print('O aluno azarado que vai ter que apagar o quadro é {}!'.format(vs))

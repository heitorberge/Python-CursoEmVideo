import random
a1 = input('Nome do aluno 1: ')
a2 = input('Nome do aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')
l = [a1, a2, a3, a4]
v1 = random.choice(l)
print(f'O primeiro aluno a apresentar será: {v1}')
l.remove(v1)
v2 = random.choice(l)
print(f'O segundo aluno a apresentar será: {v2}')
l.remove(v2)
v3 = random.choice(l)
print(f'O terceiro aluno a apresentar será: {v3}')
l.remove(v3)
v4 = l[0]
print(f'O quarto aluno a apresentar será: {v4}')
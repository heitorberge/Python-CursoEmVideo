lsita = []
while True:
    nome = input('Digite um nome: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    lsita.append([nome, [nota1, nota2], media])
    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Resposta inválida! Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for i, aluno in enumerate(lsita):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc >= len(lsita):
        print('Aluno não encontrado. Tente novamente.')
    else:
        print(f'Notas de {lsita[opc][0]} são {lsita[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
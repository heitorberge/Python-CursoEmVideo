pessoas = []
while True:
    pessoa = {}
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoas.append(pessoa.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = sum(p['Idade'] for p in pessoas) / len(pessoas)
print(f'A média de idade é de {media:.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média de idade:')
for p in pessoas:
    if p['Idade'] > media:
        print(f'  {p["Nome"]} com {p["Idade"]} anos.')
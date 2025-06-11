from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['anasc'] = int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
pessoa['idade'] = datetime.now().year - pessoa['anasc']
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contratacao'] - pessoa['anasc']) + 35
print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')

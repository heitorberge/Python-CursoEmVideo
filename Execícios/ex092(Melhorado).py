from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input(f'Ano de Nascimento : '))
dados['Idade'] = datetime.now().year - nasc
carttrab= int(input('Carteira de Trabalho (0 não tem): '))
if dados['Idade'] >= 18:
    dados['CTPS'] = carttrab
else:
    print('Você não pode ter CTPS antes dos 18 anos.')
    dados['CTPS'] = 0
if dados['CTPS'] != 0 and dados['Idade'] >= 18:
    contact = int(input('Ano de Contratação: '))
    if contact < datetime.now().year:
        dados['Contratação'] = contact
    else:
        while contact > datetime.now().year:
            contact = int(input('Ano de Contratação Inválido! Digite um ano válido: '))
        dados['Contratação'] = contact
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + (dados['Contratação'] + 35 - datetime.now().year) 
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
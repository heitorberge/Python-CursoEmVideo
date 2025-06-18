def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :return: dicionário com várias informações sobre a situação da turma.
    """
    info = {}
    info['Total'] = len(n)
    info['Maior'] = max(n)
    info['Menor'] = min(n)
    info['Média'] = sum(n)/len(n)
    if sit == True:
        if info['Média'] >= 7:
            info['Situação'] = 'Aprovado'
        elif info['Média'] < 5:
            info['Situação'] = 'Reprovado'
        else:
            info['Situação'] = 'Recuperação'
    return info

print('-' * 30)
nota = []
cont = 0
while True:
    cont += 1
    nota.append(float(input(f'{cont}ª Nota: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp not in 'SN':
            print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
resp = ''
while resp not in 'SN':
    resp = str(input('Quer ver a situação? [S/N] ')).upper().strip()[0]
    if resp not in 'SN':
        print('ERRO! Responda apenas S ou N.')
if resp == 'S':
    sit = True
else:
    sit = False
print('-' * 30)
result = notas(*nota, sit=sit)
print(f'Total de provas : {result["Total"]}')
print(f'Maior nota: {result["Maior"]}')
print(f'Menor nota: {result["Menor"]}')
print(f'Média: {result["Média"]:.1f}')
if sit == True:
    print(f'Situação: {result["Situação"]}')
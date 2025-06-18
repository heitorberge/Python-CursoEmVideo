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
resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
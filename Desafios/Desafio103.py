def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')



nj = str(input('Nome do Jogador: ')).capitalize()
ng = int(input('Número de Gols: '))
ficha(nj, ng)

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gols} gol(s).')

nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)
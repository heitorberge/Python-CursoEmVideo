Jogador = {}
Jogador['nome'] = input('Digite o nome do jogador: ')
Jogador['partidas'] = int(input(f'Quantas partidas {Jogador["nome"]} jogou? '))
Jogador['gols'] = []
for i in range(Jogador['partidas']):
    gols = int(input(f'Quantos gols Você fez na partida {i + 1}? '))
    Jogador['gols'].append(gols)
print('-=' * 30)
print(Jogador)
print('-=' * 30)
for k, v in Jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {Jogador["nome"]} jogou {Jogador["partidas"]} partidas.')
for i, v in enumerate(Jogador['gols']):
    print(f'    => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {sum(Jogador["gols"])} gols.')
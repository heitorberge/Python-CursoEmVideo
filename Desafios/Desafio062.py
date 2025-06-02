primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total_termos = 0
mais = 10

while mais != 0:
    total_termos += mais
    while cont <= total_termos:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))

print(f'Progressão finalizada com {total_termos} termos mostrados.')
print('FIM')
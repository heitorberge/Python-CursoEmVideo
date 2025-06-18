def fatorial(número, show=False):
    fatorial = número
    for c in range(número - 1, 0, -1):
        fatorial *= c
    if show:
        for c in range(número , 0, -1):
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = {fatorial}', end='')
                
    else:
       print(fatorial)

print('-' * 30)
fact = int(input('Digite um número para calcular seu fatorial: '))
most = str(input('Deseja mostrar o calculo? [S/N] ')).upper()
if most == 'S':
    most = True
else:
    most = False
fatorial(fact, most)
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
fatorial(5, True)
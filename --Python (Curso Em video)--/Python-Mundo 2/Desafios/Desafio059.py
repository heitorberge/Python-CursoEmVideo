r = 0
s = 0
while r != 5:
    n1 = int(input('Digite o 1° número: '))
    n2 = int(input('Digite o 2° número: '))
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do progama ''')
    r = int(input(''))
    if r == 1:
        s = n1 + n2
        print('{} + {} = {}'.format(n1,n2,s))
    elif r == 2:
        s = n1 * n2
        print('{} x {} = {}'.format(n1,n2,s))
    elif r == 3:
        if n1 > n2:
            print('{} > {}'.format(n1,n2))
        elif n2 > n1:
            print('{} < {}'.format(n1,n2))
        else :
            print('{} = {}'.format(n1,n2))
    elif r == 4:
        print('')
    else:
        print('')
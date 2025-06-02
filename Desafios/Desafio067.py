nt=0
cont=0
while nt >= 0:
        nt = int(input('Digite um número (Digite um valor negativo para parar): '))
        if nt < 0:
            break
        else:
            print(f'------ Tabuada do {nt} ------')
            while cont <= 10:
                print(f'     {nt} x {cont:2} = {nt * cont}')
                cont += 1
            cont = 0
            print(f'-----------------------------')
print('Fim do progama')
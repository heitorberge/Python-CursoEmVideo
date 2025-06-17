from time import sleep
def contador(inicio,fim,passo):
    print('=-'*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ',end='',flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ',end='',flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')

# Progama Principal
contador(1,10,1)
contador(10,0,2)
print('=-'*30)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini,fim,pas)
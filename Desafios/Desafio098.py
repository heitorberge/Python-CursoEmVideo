from time import sleep
def contador(início, fim, passo):
    print('-=' * 20)
    print(f'Vamos contar de {início} até {fim} de {passo} em {passo}!')
    if passo == 0:
        passo = 1
    if início < fim and passo < 0:
        passo = abs(passo)
    if início > fim and passo > 0:
        passo = -passo
    for cont in range(início, fim + 1 if passo > 0 else fim - 1, passo):
        sleep(0.5)
        print(cont, end=' ')
    print('FIM!')
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, fim, passo)
cont = soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print(f'A soma dos {cont} valores foi {soma}!')
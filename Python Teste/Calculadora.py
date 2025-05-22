res = 1
while res == 1:
    print('Calculadora!!!')
    n1 = int(input('Digite um Valor para a Calculadora: '))
    print('|÷(Ou digite /)|x|-|+|')
    s = str(input('Digite um Símbolo para a Calculadora: '))
    n2 = int(input('Digite um Valor para a Calculadora: '))
    res_calculo = 0
    if s == '÷' or '/':
        res_calculo = n1 / n2
    elif s == 'x':
        res_calculo = n1 * n2
    elif s == '-':
        res_calculo = n1 - n2
    elif s == '+':
        res_calculo = n1 + n2
    else:
        print('Símbolo Inválido!')
        continue
    print('{} {} {} = {}'.format(n1, s, n2, res_calculo))
    print('Deseja continuar?')
    print('(1) Sim')
    print('(2) Não')
    res = int(input(''))
    print('▶ Fim do programa')
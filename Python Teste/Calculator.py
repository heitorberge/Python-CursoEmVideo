res = 1
while res == 1:
    print('Calculator!!!')
    n1 = int(input('Enter a Value for the Calculator: '))
    print('|÷(Or type /)|x|-|+|')
    s = str(input('Enter a Symbol for the Calculator: '))
    n2 = int(input('Enter a Value for the Calculator: '))
    res_calculo = None
    if s == '÷' or '/':
        res_calculo = n1 / n2
    elif s == 'x':
        res_calculo = n1 * n2
    elif s == '-':
        res_calculo = n1 - n2
    elif s == '+':
        res_calculo = n1 + n2
    else:
        print('Invalid Symbol!')
        continue
    print('{} {} {} = {}'.format(n1, s, n2, res_calculo))
    print('Do you want to continue?')
    print('(1) Yes')
    print('(2) No')
    res = int(input(''))
print('▶ End of program')
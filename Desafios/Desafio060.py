num = int(input('Digite um número: '))
fat = 1
print('{}! = '.format(num), end='')
if num == 0:
    print('1')
elif num == 1:
    print('1')
else:
    for i in range(num, 0, -1):
        fat *= i
        print(i, end='')
        if i > 1:
            print(' x ', end='')
    print(' = {}'.format(fat))
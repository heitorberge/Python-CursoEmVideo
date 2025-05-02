n1 = int(input('Primeiro número: '))
n2 = int(input('\033[0:34mSegundo número: \033[0:30m'))
if n1 > n2:
    print('O \033[0:31mPRIMEIRO\033[0:30m valor é maior.')
elif n2 > n1:
    print('O \033[0:31mSEGUNDO\033[0:30m valor é maior.')
else:
    print('Não existe valor maior, os dois são \033[0:31mIGUAIS\033[0:30m.')
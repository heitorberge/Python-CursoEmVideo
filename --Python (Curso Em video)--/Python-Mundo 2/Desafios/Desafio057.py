R = ''
while R != 'M' and R != 'F':
    R = str(input('Digite o sexo da pessoa: ')).upper()
    if R != 'M' and R != 'F':
        print('Erro! Digite apenas M ou F.')

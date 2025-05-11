n = int(input('Digite um valor: '))
if n <= 1:
    print('O número não é Primo')
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print('O número não é Primo')
    print('O número é Primo')
n = s = 1
while n != 999:
    n = int(input('Digite um número:  '))
    if n == 999:
        break
    else:
        s += n
print(f'A soma vale {s}')
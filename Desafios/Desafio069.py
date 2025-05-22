id18 = 0
hm = 0
mm = 0
res = 'S'
while res == 'S':
    idade = int(input('Idade da Pessoa: '))
    sexo = str(input('Sexo da Pessoa (M/F): ')).upper().strip()[0]
    if idade > 18:
        id18 += 1
    if sexo == 'M':
        hm += 1
    if sexo == 'F' and idade < 20:
        mm += 1
    res = str(input('Deseja continuar? (S/N) ')).upper().strip()[0]
print(f'{id18} pessoas tem mais de 18 anos.')
print(f'{hm} homens foram cadastrados.')
print(f'{mm} Mulheres tem menos de 20 anos.')
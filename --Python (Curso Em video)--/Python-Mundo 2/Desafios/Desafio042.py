print('-=' * 13)
print(' Analisador de Triângulos')
print('-=' * 13)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if r1 == r2 == r3:
        print('Este triângulo é EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Este triângulo é ISÓSCELES!')
    else:
        print('Este triângulo é ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
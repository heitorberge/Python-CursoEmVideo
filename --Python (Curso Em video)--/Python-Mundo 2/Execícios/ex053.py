frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('Você digitou a frase {} e o inverso dela é {}'.format(junto,inverso))
if inverso == junto:
    print('Esta frase é um palíndromo!')
else:
    print('Esta frase não é um palíndromo!')
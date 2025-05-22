frase = str(input('Digite uma frase: ')).upper().strip()
frase = frase.replace(" ", "")
tamanho = len(frase)
ep = True

for i in range(tamanho // 2):
    if frase[i] != frase[tamanho - 1 - i]:
        ep = False
        break

if ep:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
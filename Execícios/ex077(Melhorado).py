palavra = input('Digite uma palavra: ').strip()
palavras = tuple(palavra.split())
for palavra in palavras:
    print(f'Na palavra "{palavra.upper()}" temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aáàãâeéèêiíìîoõóòôuúùû':
            print(letra, end=' ')
    print(';')

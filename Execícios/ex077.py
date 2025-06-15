palavras = ('aprender', 'programar', 'linguagem', 'python', 
            'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'\nNa palavra "{palavra.upper()}" temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aáàãâeéèêiíìîoõóòôuúùû':
            print(letra, end=' ')
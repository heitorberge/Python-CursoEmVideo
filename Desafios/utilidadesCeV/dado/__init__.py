def leiaDinheiro(msg):
    """
    Função para ler um valor monetário do usuário.
    :param msg: Mensagem a ser exibida ao usuário.
    :return: Valor monetário validado.
    """
    while True:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! "{entrada}" é um preço inválido.\033[m')
        else:
            try:
                valor = float(entrada)
                return valor
            except ValueError:
                print(f'\033[0;31mERRO! "{entrada}" é um preço inválido.\033[m')
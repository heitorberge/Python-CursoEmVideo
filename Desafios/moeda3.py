def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')
def aumentar(preco, taxa, format=False):
    """
    Aumenta o preço por uma taxa percentual.
    
    :param preco: Preço original.
    :param taxa: Taxa percentual a ser aplicada.
    :return: Preço com aumento.
    """
    if format:
        return f'{moeda(preco + (preco * taxa / 100))}'
    else:
        return preco + (preco * taxa / 100)
def diminuir(preco, taxa, format=False):
    """
    Diminui o preço por uma taxa percentual.
    :param preco: Preço original.
    :param taxa: Taxa percentual a ser aplicada.
    :return: Preço com desconto.
    """
    if format:
        return f'{moeda(preco - (preco * taxa / 100))}'
    else:
        return preco - (preco * taxa / 100)
def dobro(preco, format=False):
    """
    Calcula o dobro do preço.
    :param preco: Preço original.
    :return: Dobro do preço.
    """
    if format:
        return f'{moeda(preco * 2)}'
    else:
        return preco * 2
def metade(preco, format=False):
    """
    Calcula a metade do preço.
    :param preco: Preço original.
    :return: Metade do preço.
    """
    if format:
        return f'{moeda(preco / 2)}'
    else:
        return preco / 2
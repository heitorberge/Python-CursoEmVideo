def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')
def aumentar(preco, taxa):
    """
    Aumenta o preço por uma taxa percentual.
    
    :param preco: Preço original.
    :param taxa: Taxa percentual a ser aplicada.
    :return: Preço com aumento.
    """
    return preco + (preco * taxa / 100)
def diminuir(preco, taxa):
    """
    Diminui o preço por uma taxa percentual.
    :param preco: Preço original.
    :param taxa: Taxa percentual a ser aplicada.
    :return: Preço com desconto.
    """
    return preco - (preco * taxa / 100)
def dobro(preco):
    """
    Calcula o dobro do preço.
    :param preco: Preço original.
    :return: Dobro do preço.
    """
    return preco * 2
def metade(preco):
    """
    Calcula a metade do preço.
    :param preco: Preço original.
    :return: Metade do preço.
    """
    return preco / 2
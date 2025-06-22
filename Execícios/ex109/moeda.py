def aumentar(preço=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o valor com ou sem formatação monetária.
    :param preço: O preço a ser aumentado.
    :param taxa: A porcentagem de aumento.
    :param formato: Se True, retorna o valor formatado como moeda.
    :return: O valor aumentado, formatado ou não.
    """
    res = preço + (preço * taxa / 100)
    return moeda(res) if formato else res

def diminuir(preço=0, taxa=0, formato=False):
    """
    -> Calcula a redução de um determinado preço,
    retornando o valor com ou sem formatação monetária.
    :param preço: O preço a ser reduzido.
    :param taxa: A porcentagem de redução.
    :param formato: Se True, retorna o valor formatado como moeda.
    :return: O valor reduzido, formatado ou não.
    """
    res = preço - (preço * taxa / 100)
    return moeda(res) if formato else res
def dobro(preço=0, formato=False):
    """
    -> Calcula o dobro de um determinado preço,
    retornando o valor com ou sem formatação monetária.
    :param preço: O preço a ser dobrado.
    :param formato: Se True, retorna o valor formatado como moeda.
    :return: O valor dobrado, formatado ou não.
    """
    res = preço * 2
    return moeda(res) if formato else res

def metade(preço=0, formato=False):
    """
    -> Calcula a metade de um determinado preço,
    retornando o valor com ou sem formatação monetária.
    :param preço: O preço a ser dividido.
    :param formato: Se True, retorna o valor formatado como moeda.
    :return: O valor dividido, formatado ou não.
    """
    res = preço / 2
    return moeda(res) if formato else res

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
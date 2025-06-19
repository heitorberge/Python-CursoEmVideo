def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
        f *= c
    return f


# print(fatorial(5,True))
help(fatorial)
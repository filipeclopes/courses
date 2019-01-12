def soma(x, y):
    """
    Soma dois números com posições.

    Arg:
        - x: inteiro
        - y: inteiro
    """
    return x + y


def soma_2(x=3, y=7.5):
    """
    Soma dois números com valores opicionaiz.

    Arg:
        - x: inteiro
        - y: inteiro
    """
    return x + y

def soma_3(*batman):
    """
    soma_3 soma uma quantidade indefinida de números.

    Arg:
        - batman: números
    """
    return sum(batman)


def soma_4(**robin):
    """
    soma_4 soma uma quantidade indefinida de números.

    Arg:
        - robin: números nomeados
    """
    return sum(robin.values())

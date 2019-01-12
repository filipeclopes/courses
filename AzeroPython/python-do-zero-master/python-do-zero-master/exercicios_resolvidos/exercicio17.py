"""
Exercício #17
Faça um programa, com uma função, que calcula a mediana de uma lista.
Funções embutidas que podem te ajudar:
    sorted(lista) -> ordena a lista
"""


def mediana(lista):
    tamanho = len(lista)
    lista_ordenada = sorted(lista)
    central = tamanho//2

    if tamanho % 2:
        return lista_ordenada[central]
    else:
        baixo = central - 1
        alto = central
        return (lista_ordenada[baixo] + lista_ordenada[alto]) / 2

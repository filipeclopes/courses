"""
Exercício #16
Faça um programa, com uma função, que calcula a média de uma lista.
Funções embutidas que podem te ajudar:
    len(lista) -> calcula o tamanho da lista
    sum(lista) -> faz o somatório dos valores
"""


def media(lista):
    return sum(lista)/len(lista)


print(media([1,2,3,4]))

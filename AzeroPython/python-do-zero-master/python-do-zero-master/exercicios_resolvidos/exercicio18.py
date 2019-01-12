"""
Exercício #18
Faça um programa, com uma função que dado uma lista e uma posição da mesma faça o quantil dessa posição.

p_index = int(ponto * len(lista))
"""


def quantil(lista, ponto):
    p_index = int(ponto * len(lista))
    return sorted(lista)[p_index]

print(quantil([1, 2, 3, 4, 5], 0.90))

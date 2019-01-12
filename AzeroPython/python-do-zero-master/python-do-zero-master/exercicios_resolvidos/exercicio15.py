"""
Exercício #15
Faça um programa que dada a entrada de uma lista ele calcule as combinações e
nos retorne as combinações em uma nova lista.
Exemplo de entrada: [1, 2, 3, 4]
Exemplo de saida: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
"""
lista = [1, 2, 3, 4]
# Com combinatória total
print([[x, y] for x in lista for y in lista])

# Repetições com biblioteca
from itertools import combinations_with_replacement
print(list(combinations_with_replacement(lista, 2)))

# Sem repetições com biblioteca
from itertools import combinations
print(list(combinations(lista, 2)))

# Uma variação que fizemos em sala
print([[x, y] for x in lista[::2] for y in lista[1::2]])

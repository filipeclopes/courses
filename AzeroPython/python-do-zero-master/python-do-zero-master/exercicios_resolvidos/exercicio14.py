"""
Exercício #14
Faça uma programa que dada a entrada de uma lista ele faça o calculo
acumulativo da mesma:
Exemplo de entrada: [1, 2, 3, 4]
Exemplo de saída: [1, 3, 6, 10]
"""
lista = [1, 2, 3, 4]
print([sum(lista[:y]) for y in range(1, len(lista) + 1)])

# Maneira com bibliotecas prontas
from itertools import accumulate
print(list(accumulate(lista)))

# Maneira com for
saida = []
for index, numero in enumerate(lista):
    saida.append(sum(lista[:index + 1]))

print(saida)

"""
Exercício #13
Faça um programa que: Dada uma lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e um número
inteiro, imprima a tabuada desse número.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input('Digite um número: '))

# Maneira com for
for numero in lista:
    print(n * numero)

# Maneira com copreenção de listas
print([n * numero for numero in lista])

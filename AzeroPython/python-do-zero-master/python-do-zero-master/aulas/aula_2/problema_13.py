"""
Dada uma lista [1..10].

e um numero inteiro, imprima a tabuada desse numero.
"""

# lista = range(1, 11)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
número = int(input('Digite um número inteiro: '))

for m in lista:
    print(f'{número} x {m} = {número * m}')

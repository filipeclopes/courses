"""
Exercício # 12
Faça um programa que receba uma string, com um número de ponto flutuante, e
imprima qual a parte dele que não é inteira
EX:
n = ‘3.14’
responsta: 14
"""
numero = input('Digite um número de ponto flutuante: ')

# Maneira rápida
print(numero.split('.')[1])

# Maneira com for
ponto = False
for c in numero:
    if ponto:
        print(c)

    if c == '.':
        ponto = True

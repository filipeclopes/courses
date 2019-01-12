"""
Exercício # 11
Faça um programa que itere em uma string e toda vez que uma vogal aparecer
na sua string print o seu nome entre as letras
string = bananas
b
eduardo
n
eduardo
n
...
"""
string = input('Digite uma string: ')
nome = input('Digite seu nome: ')

for letra in string:
    if letra in 'aeiou':
        print(nome)
    else:
        print(letra)

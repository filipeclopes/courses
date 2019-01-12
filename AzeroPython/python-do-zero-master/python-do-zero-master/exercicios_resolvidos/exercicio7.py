"""
Exercício #7
Faça um programa que receba uma string e responda se ela tem alguma vogal,
se sim, quais são? E também diga se ela é uma frase ou não.
"""

palavra = input('Digite uma palavra: ')

if 'a' in palavra or 'e' in palavra or 'i' in palavra or \
    'o' in palavra or 'u' in palavra:
    print('palavra tem vogais')

    if 'a' in palavra:
        print('palavra tem a')

    if 'e' in palavra:
        print('palavra tem e')

    if 'i' in palavra:
        print('palavra tem i')

    if 'o' in palavra:
        print('palavra tem o')

    if 'u' in palavra:
        print('palavra tem u')

if ' ' in palavra:
    print('É uma frase')

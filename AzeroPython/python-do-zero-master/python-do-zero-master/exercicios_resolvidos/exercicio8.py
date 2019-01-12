"""
Exercício #8
Faça um programa que receba uma data de nascimento (15/07/87) e imprima
'Você nasceu em <dia> de <mes> de <ano>'
"""

data = input('Digite sua data de nascimento: ')

dia, mes, ano = data.split('/')

print('Você nasceu em {} de {} de {}'.format(dia, mes, ano))

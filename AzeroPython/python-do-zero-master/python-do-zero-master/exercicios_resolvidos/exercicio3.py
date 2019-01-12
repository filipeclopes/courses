"""
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total.
"""
metros = input("Digite a quantidade de metros quadrados a serem pintados: ")
litros = int(metros)/3

preço = 80.0
capacidadeL = 18

latas = litros / capacidadeL
preço_total = latas * preço

print(f'Você usara {latas}, latas de tinta')
print(f'O preco total é de: R$ {preço_total}')

"""
Caso você queira fazer o arredondamento correto
No python, a biblioteca interna te matemática tem uma função chamada
ceil que faz esse arredondamento
"""
from math import ceil
print("""

medidas arredondadas

""")
print(f'Você usara {ceil(latas)}, latas de tinta')
print(f'O preco total é de: R$ {ceil(preço_total)}')

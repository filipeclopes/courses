"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e
    continue pedindo até que o usuário informe um valor válido.
"""

cond = False

# Olhar antes de saltar
while not cond:
    nota = input('Insira uma nota entre 0 e 10: ')
    if nota.isdigit():
        if float(nota) >= 0 and float(nota) < 11:
            cond = True
    print('Olá coleguinha, insira um valor válido')


# Melhor pedir perdão
while not cond:
    nota = input('Insira uma nota entre 0 e 10: ')
    try:
        nota = float(nota)
        if float(nota) >= 0 and float(nota) < 11:
            cond = True
    except:
        print('Olá coleguinha, insira um valor válido')



print(f'Você inseriu {nota}, um valor válido')

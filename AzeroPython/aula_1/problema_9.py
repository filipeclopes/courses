nota = input('Insira uma nota entre zero e dez: ')

while not nota.isdigit():
    print('Insira um valor válido')
    nota = input('Insira uma nota entre zero e dez: ')

print(f'Você inseriu {nota}, um valor válido')

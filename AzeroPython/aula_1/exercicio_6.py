produto1 = int(input('Informe o valor do produto 1: '))
produto2 = int(input('Informe o valor do produto 2: '))
produto3 = int(input('Informe o valor do produto 3: '))

prodEscolhido = produto1

if produto2 < prodEscolhido and produto2 < produto3:
    prodEscolhido = produto2
if produto3 < prodEscolhido and produto3 < produto2:
    prodEscolhido = produto3

print(f'Compre o produto de valor {prodEscolhido}')

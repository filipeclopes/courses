"""
Exercício #21
Dada uma lista de entradas de usuário de números inteiros, construa um dicionário com a lista padrão, a lista dos valores elevados ao quadrado e a lista dos valores elevados ao cubo
"""
lista = []
dicionario = {}
cond = 'S'


def cubo(lista):
    return [x**3 for x in lista]

def quadrado(lista):
    return [x**2 for x in lista]


while cond == 'S' or cond == 's':
    lista.append(int(input('Digite um valor: ')))
    cond = input('Deseja inserir outro valor: (s/n)')

dicionario['lista'] = lista
dicionario['lista ao quadrado'] = quadrado(lista)
dicionario['lista ao cubo'] = cubo(lista)

print(dicionario)

"""
Exercício #20
Baseando-se nos exercícios passados, monte um dicionário com os seguintes seguintes chaves:
lista, somatório, tamanho, maior valor e menor valor

o exiba na tela
"""
lista = [1, 2, 3, 4, 5, 6]
dicionario = {}
dicionario['lista'] = lista
dicionario['somatório'] = sum(lista)
dicionario['tamanho'] = len(lista)
dicionario['maior valor'] = max(lista)
dicionario['menor valor'] = min(lista)

print(dicionario)

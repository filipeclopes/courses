#...
#Data uma lista [1..10]
#e um numero inteiro, imprima a tabuada desse numero
#...

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#lista = range(1,11)
numero = int(input('Digite um numero inteiro: '))

for m in lista:
    print(f'{numero} x {m} = {numero * m}')

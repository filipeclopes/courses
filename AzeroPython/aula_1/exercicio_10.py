contador = 0
maior = 0

while contador < 5:
    numero = int(input('Digite um número: '))
    if numero > maior:
        maior = numero
    contador += 1

print(f'O maior número é: {maior}')

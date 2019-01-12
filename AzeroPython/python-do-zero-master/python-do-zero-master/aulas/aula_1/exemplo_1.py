n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

print(type(n1))

if n1 == n2:
    print(f'{n1} e {n2} são iguais')
elif n1 > n2:
    print(f'{n1} é maior que {n2}')
else:
    print(f'Não sei responder pra {n1} e {n2}')

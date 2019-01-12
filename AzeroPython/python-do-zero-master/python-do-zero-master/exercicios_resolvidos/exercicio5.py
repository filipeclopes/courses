"""
Exercício #5
Faça um programa para a leitura de duas notas parciais de um aluno. O programa
deve calcular a média alcançada por aluno e apresentar:

    1. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    2. A mensagem "Reprovado", se a média for menor do que sete;
    3. A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
nota_1 = int(input('Digite a primeira nota: '))
nota_2 = int(input('Digite a primeira nota: '))

media = (nota_1 + nota_2)/2

print(media)

if media == 10:
    print('Aprovado com Distinção')

elif media < 10 and media >= 7:
    print('Aprovado')

else:
    print('Reprovado')

"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
import statistics

nota_1 = float(input('Nota um do aluno: '))
nota_2 = float(input('Nota dois do aluno: '))

# média = statistics.median([nota_1, nota_2])
média = sum([nota_1, nota_2]) / 2


if média == 10:
    print('Aprovado com Distinção')
elif média >= 7:
    print('Aprovado')
elif média < 7:
    print('Reprovado')

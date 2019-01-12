nota_1 = float(input('Nota um do aluno: '))
nota_2 = float(input('Nota um do aluno: '))
# import statistics

media = sum([nota_1, nota_2]) / 2
# media = statistics.median([nota_1, nota_2])
if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')

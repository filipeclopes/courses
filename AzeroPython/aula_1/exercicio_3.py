area = float(input('Informe a área a ser pintada em m2: '))

litrosNecessarios = area/3

latasNecessarias = int(-(-litrosNecessarios//18))
custo = latasNecessarias * 80
print(f'Você precisa de {latasNecessarias} e o custo é de {custo}')

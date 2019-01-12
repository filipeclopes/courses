dtNascimento = input('Informe uma data de nascimento (dd/mm/aaaa)')
dia, mes, ano = dtNascimento.split('/')

print('Você nasceu em {} de {} de {}'.format(dia, mes, ano))

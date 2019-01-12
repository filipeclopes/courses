preço_prod_1 = int(input("Digite o 1° preço: "))
preço_prod_2 = int(input("Digite o 2° preço: "))
preço_prod_3 = int(input("Digite o 3° preço: "))

if preço_prod_1 < preço_prod_2 and preço_prod_3 and preço_prod_1:
    print('O produto 1 é o mais barato!!')
elif preço_prod_2 < preço_prod_1 and preço_prod_3:
    print('O produto 2 é o mais barato!!')
elif preço_prod_3 < preço_prod_1 and preço_prod_2:
    print('O produto 3 é o mais barato!!')

# Se alguns numeros forem iguais
elif preço_prod_1 == preço_prod_2 and preço_prod_1 and preço_prod_2 < preço_prod_3:
    print('O produto 1 e 2 são os mais baratos!!')
elif preço_prod_1 == preço_prod_3 and preço_prod_1 and preço_prod_3 < preço_prod_2:
    print('O produto 1 e 3 são os mais baratos!!')
elif preço_prod_2 == preço_prod_3 and preço_prod_2 and preço_prod_3 < preço_prod_1:
    print('O produto 1 e 2 são os mais baratos!!')

# Se todo os numero forem iguais
else:
    print('Todos os preços são iguais!!')

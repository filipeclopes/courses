palavra = input('Insira uma palavra qualquer: ')


def conta_vogais(palavra):
    palavra = palavra.lower()
    vogais = 'aeiou'
    return {i: palavra.count(i) for i in vogais}


print(conta_vogais(palavra))

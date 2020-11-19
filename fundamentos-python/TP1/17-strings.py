# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/fundamentos-python/TP1
# Escreva uma função que receba uma string e um número inteiro x e rotacione
# a string x posições para a esquerda. Assuma que a string tem pelo menos x caracteres.

# Isto é, utilizando como entradas a string “aeiou” e o inteiro 3,
# o resultado da sua função deve ser “ouaei”.

campos = [
    {'label': 'Informe uma string qualquer:', 'valor': 0},
    {'label': 'Informe um o tamanho de caracteres:', 'valor': 0},
]

def inverte_string(string, ponto_inversao):
    if ponto_inversao.isnumeric():
        ponto_inversao = int(ponto_inversao)
    else: return 'O tamanho de caracteres precisa ser um número inteiro'

    return string[ponto_inversao:] + string[:ponto_inversao]

for campo in campos:
    while True:
        campo['valor'] = input(f"{campo['label']} ") or ''

        if(not campo['valor']):
            print("O valor informado é inválido.")
        else:
            break

print(inverte_string(campos[0]['valor'], campos[1]['valor']))

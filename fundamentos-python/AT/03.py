# Usando o Thonny, escreva uma função em Python chamada potencia.
# Esta função deve obter como argumentos dois números inteiros,
# A e B, e calcular AB usando multiplicações sucessivas
# (não use a função de python math.pow) e retornar o resultado da operação.
# Depois, crie um programa em Python que obtenha dois números inteiros do
# usuário e indique o resultado de AB usando a função.
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/AT/
campos = [
    {'label': 'Informe um número inteiro a ser usado como base:', 'valor': 0},
    {'label': 'Informe um número inteiro a ser usado como expoente:', 'valor': 0},
]


def potencia(base, expoente):
    base, expoente = int(base), int(expoente)

    resultado = base
    for n in range(1, expoente):
        print(resultado, expoente)
        resultado *= base

    return resultado


for campo in campos:
    while True:
        campo['valor'] = input(f"{campo['label']} ") or ''

        if not campo['valor'].isnumeric():
            print("O valor informado é inválido.")
        elif not int(campo['valor']) > 0:
            print(f"O valor precisa ser maior que zero.")
        else:
            break

print(
    f"A potenciação da base {campos[0]['valor']} e expoente {campos[1]['valor']} é: {potencia(campos[0]['valor'], campos[1]['valor'])}")

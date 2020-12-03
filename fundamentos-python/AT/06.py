# Escreva uma função em Python que leia uma tupla contendo números inteiros,
# retorne uma lista contendo somente os números ímpares e uma nova tupla contendo
# somente os elementos nas posições pares.
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/AT/

n = (17, 37, 3, 34, 35, 94, 23, 75, 46, 75, 92, 28, 63, 66, 32, 19, 91, 96, 29, 44)


def pares_impares(numeros):
    items_pares, impares = [], []

    for index, numero in enumerate(numeros):
        if index % 2 == 0:
            items_pares.append(numero)

        if numero % 2 != 0:
            impares.append(numero)

    return [impares, tuple(items_pares)]


print(pares_impares(n))

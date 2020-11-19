# Escreva um programa em Python que leia um vetor de 5 números inteiros e mostre-os
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/TP3/

numeros = []
for i in range(1, 6):

    while True:
        data = input(f"Informe um número inteiro: ")
        data = int(data) if data.isnumeric() else False

        if not data:
            print(f"O valor informado é inválido")
        else:
            numeros.append(data)
            break

print(numeros)

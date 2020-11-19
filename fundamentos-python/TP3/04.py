# Escreva um programa em Python que leia um vetor de números de tamanho t.
# Leia t previamente. Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele.
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/TP3/

tamanho = 0
numeros = []

while True:
    data = input(f"Quantas vezes deve ser executado? ")
    data = int(data) if data.isnumeric() else False

    if not data:
        print(f"O valor informado é inválido")
    else:
        tamanho = data
        break

for n in range(0, tamanho):
    while True:
        data = input(f"Informe um número inteiro ({n + 1} de {tamanho}): ")
        data = int(data) if data.isnumeric() else False

        if data is False:
            print(f"O valor informado é inválido")
        else:
            numeros.append(data)
            break

print(f"Existem {numeros.count(0)} ocorrências do número zero na lista")

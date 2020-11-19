# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/fundamentos-python/TP1
# Escreva uma função em Python que some todos os números ímpares de 1 até um dado N, inclusive.
# O número N deve ser obtido do usuário. Ao final, escreva o valor do resultado desta soma.

def soma_impares(limite):
    soma = 0
    for n in range(1, limite + 1):
        if n % 2 != 0:
            soma += n

    return soma

while True:
    data = input(f"Informe um número inteiro: ")
    data = int(data) if data.isnumeric() else False

    if data:
        print(f"A soma dos números ímpares entre 1 e {data} é: {soma_impares(data)}")
        break

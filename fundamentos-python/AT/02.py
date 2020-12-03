# Usando o Thonny, escreva um programa em Python que some todos os
# números pares de 1 até um dado n, inclusive. O dado n deve ser
# obtido do usuário. No final, escreva o valor do resultado desta soma.
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/AT/

def soma_pares(limite):
    soma = 0
    for n in range(1, limite + 1):
        if n % 2 == 0:
            soma += n

    return soma


while True:
    data = input(f"Informe um número inteiro: ")
    data = int(data) if data.isnumeric() else False

    if data:
        print(f"A soma dos números pares entre 1 e {data} é: {soma_pares(data)}")
        break

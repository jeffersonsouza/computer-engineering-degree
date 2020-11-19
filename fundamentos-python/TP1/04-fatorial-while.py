# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/fundamentos-python/TP1
# Escreva uma função em Python que calcule o fatorial de um dado número N usando um for.
# O fatorial de N=0 é um. O fatorial de N é (para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1.
# Por exemplo, para N=5 o fatorial é: 5 x 4 x 3 x 2 x 1 = 120.
# Se N for negativo, exiba uma mensagem indicando que não é possível calcular seu fatorial.

campos = [
    {'label': 'Informe um número inteiro:', 'valor': 0},
]

def calcula_fatorial(numero):
    numero = int(numero)
    resultado = 1
    calc = ''
    while numero >= 1:
        calc += f"{numero} {'x' if numero > 1 else '='} "
        resultado *= numero
        numero -= 1

    return calc + str(resultado)

for campo in campos:
    while True:
        campo['valor'] = input(f"{campo['label']} ") or ''

        if(not campo['valor'].isnumeric()):
            print("O valor informado é inválido.")
        elif(not int(campo['valor']) > 0):
            print(f"Não é possível calcular o fatorial de {campo['valor']}.")
        else:
            break

print(f"O cálculo fatorial de {campos[0]['valor']} é:", calcula_fatorial(campos[0]['valor']))

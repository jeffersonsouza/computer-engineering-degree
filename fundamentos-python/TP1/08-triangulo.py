# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/fundamentos-python/TP1
# Escreva um programa em Python que receba três valores reais X, Y e Z, guarde esses valores numa tupla e
# verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, neste caso,
# retorne qual o tipo de triângulo formado.

# Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita:
# o comprimento de cada lado de um triângulo deve ser menor do que a soma do comprimento dos outros dois lados.

# Além disso, o programa deve identificar o tipo de triângulo formado observando as seguintes definições:
# - Triângulo Equilátero: os comprimentos dos três lados são iguais.
# - Triângulo Isósceles: os comprimentos de dois lados são iguais.
# - Triângulo Escaleno: os comprimentos dos três lados são diferentes.

campos = [
    {'label': 'Informe um o tamanho do primeiro lado do triângulo:', 'valor': 0},
    {'label': 'Informe um o tamanho do segundo lado do triângulo:', 'valor': 0},
    {'label': 'Informe um o tamanho do terceiro lado do triângulo:', 'valor': 0},
]

def calcula_tipo_triangulo(x, y, z):
    triangulo = tuple((int(x), int(y), int(z)))
    tipo = False
    for n in triangulo:
        if n > (sum(triangulo) - n):
            return 'Os valores informados não configuram um triângulo'

        if triangulo.count(n) == 3:
            tipo = 'Equilátero'
        elif triangulo.count(n) == 2:
            tipo = 'Isósceles'

    if not tipo: tipo = 'Escaleno'

    return tipo

for campo in campos:
    while True:
        campo['valor'] = input(f"{campo['label']} ") or ''

        if(campo['valor'].isalpha()):
            print("O valor informado é inválido.")
        else:
            break

print(calcula_tipo_triangulo(campos[0]['valor'], campos[1]['valor'], campos[2]['valor']))

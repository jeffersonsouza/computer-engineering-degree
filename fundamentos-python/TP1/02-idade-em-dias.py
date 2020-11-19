# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/fundamentos-python/TP1
# Faça uma função em Python que receba do usuário a idade de uma pessoa em anos, meses e dias
# e retorne essa idade expressa em dias. Considere que todos os anos têm 365 dias.

campos = [
    {'label': 'Informe a quantidade de anos:', 'valor': 0},
    {'label': 'Informe a quantidade de meses:', 'valor': 0},
    {'label': 'Informe a quantidade de dias:', 'valor': 0},
]

def converte_idade_dias(anos, meses, dias):
    anos, meses, dias = int(anos), int(meses), int(dias)

    return (anos * 365) + (meses * 30) + dias

for campo in campos:
    while True:
        campo['valor'] = input(f"{campo['label']} ") or 0

        if(not campo['valor'].isnumeric()):
            print("O valor informado é inválido.")
        else:
            break

print(f"A sua idade, em dias, é de aproximadamente {converte_idade_dias(campos[0]['valor'], campos[1]['valor'], campos[2]['valor'])} dias e contando...")

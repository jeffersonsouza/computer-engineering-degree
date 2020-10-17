campos = [
    {'label': 'Informe o multiplicador', 'valor': 0},
    {'label': 'Informe o valor de inicio:', 'valor': 1},
    {'label': 'Informe o valor de fim:', 'valor': 10},
]

def gera_tabuada(multiplicador, inicio = 1, fim = 10):
    multiplicador, inicio, fim = int(multiplicador), int(inicio), int(fim)

    for n in range(inicio, fim + 1):
        print(f"{multiplicador} x {n} = {multiplicador * n}")
    return

for campo in campos:
    while True:
        # Pergunta e valida os dados
        campo['valor'] = input(f"{campo['label']} ") or 0

        if(not campo['valor'].isnumeric()):
            print("O valor informado é inválido.")
        else:
            break

gera_tabuada(campos[0]['valor'], campos[1]['valor'], campos[2]['valor'])

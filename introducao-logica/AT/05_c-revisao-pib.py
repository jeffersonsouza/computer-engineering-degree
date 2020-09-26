# ENUNCIADO:
# Desenvolva uma função que, para um país, exiba o gráfico da evolução do PIB ao longo dos anos.
# A função deve receber, como entrada, o nome de um país, e exibir o gráfico para todo o período listado na tabela.
# O gráfico deve conter os valores do PIB no eixo das ordenadas (vertical) e os anos no eixo das abscissas (horizontal)
#
# código também disponível em:
# https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/introducao-logica/AT/05_c-revisao-pib.py

import matplotlib.pyplot as plt
import numpy as np

campos = [
    {'label': 'Informe um país:', 'valor': 0},
]

arquivo = open('assessment-pibs.csv', 'r')
paises_pibs = arquivo.read()
paises_pibs = paises_pibs.splitlines()
arquivo.close() # já que não vou mais precisar ler o arquivo, ele pode ser fechado logo aqui

def gera_grafico_projecao_pib(pais):

    anos = paises_pibs[0].split(',')
    for pais_pib in paises_pibs:
        pais_pib = pais_pib.split(',')
        if(pais_pib[0].lower() == pais.lower()):
            print(pais_pib[1:])
            print(anos[1:])
            eixo_x = anos[1:]
            eixo_y = np.array(pais_pib[1:])

            plt.plot(eixo_x, eixo_y.astype(float))
            plt.xlabel('Ano')
            plt.ylabel('Valor US$ (em Trilhões)')
            plt.title(f"{pais_pib[0]} - Evolução de PIB")
            plt.show()

            return

    print('País não disponível')
    return

for campo in campos:
    while True:
        # Pergunta e valida os dados
        campo['valor'] = input(f"{campo['label']} ")

        if(not campo['valor']):
            print("O valor informado é inválido.")
        else:
            break

gera_grafico_projecao_pib(campos[0]['valor'])

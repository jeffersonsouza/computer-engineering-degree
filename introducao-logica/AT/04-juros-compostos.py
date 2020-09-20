# ENUNCIADO:
# Assim, suponha que você possui R$10.000 iniciais, consegue aportar R$1.000 por mês e obtém um rendimento
# de 0,54% ao mês. Por simplicidade, suponha que você faz o aporte após o rendimento no período acontecer.
#
# No primeiro mês, terá R$10.000 + 0,54% deste valor = R$10.054,00. E, com o novo aporte, R$11.054,00.
#
# Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, como entrada,
# um montante financeiro inicial, um percentual de rendimento por período, um valor de aporte para
# cada período e uma quantidade de períodos

# código também disponível em:
# https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/introducao-logica/AT/04-juros-compostos.py

import matplotlib.pyplot as plt

campos = [
    {'label': 'Valor inicial: R$', 'valor': 0},
    {'label': 'Rendimento por período (%):', 'valor': 0},
    {'label': 'Aporte a cada período: R$', 'valor': 0},
    {'label': 'Total de períodos:', 'valor': 0},
]

def calculo_juros(valor_inicial, rendimento_periodo, aporte_periodo, periodos):
    valor_inicial = float(valor_inicial + '.0')
    rendimento_periodo = float(rendimento_periodo)
    aporte_periodo = float(aporte_periodo + '.0')
    periodos = int(periodos)

    valor_inicio_periodo = valor_inicial

    # Para a geração do gráfico
    periodos_eixo_x = []
    valores_eixo_y = []

    for periodo in range(1, periodos + 1):
        rendimento = valor_inicio_periodo * rendimento_periodo / 100
        valor_final_periodo = valor_inicio_periodo + rendimento + aporte_periodo
        valor_inicio_periodo = valor_final_periodo
        periodos_eixo_x.append(int(periodo))
        valores_eixo_y.append(float(valor_final_periodo))
        print(f"Após {periodo} períodos(s), o montante será de R$ {round(valor_final_periodo, 2)}.")

    return [periodos_eixo_x, valores_eixo_y]

def criar_grafico(eixo_x, eixo_y):
    plt.plot(eixo_x, eixo_y)
    plt.xlabel('Periodos (meses)')
    plt.ylabel('Valor (R$)')
    plt.title('Projeção dos Juros Compostos')

    plt.show()

for campo in campos:
    while True:
        # Pergunta e valida os dados
        campo['valor'] = input(f"{campo['label']} ") or '0'

        if(not campo['valor'].replace(',', '').replace('.', '').isnumeric() or float(campo['valor']) <= 0):
            print("O valor informado é inválido.")
        else:
            break

dados_grafico = calculo_juros(campos[0]['valor'], campos[1]['valor'], campos[2]['valor'], campos[3]['valor'])

criar_grafico(dados_grafico[0], dados_grafico[1])

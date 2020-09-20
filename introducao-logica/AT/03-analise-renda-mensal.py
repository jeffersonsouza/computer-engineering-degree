# ENUNCIADO:
#
# Crie um programa contendo uma função que, dados um valor de renda mensal total,
#  gastos totais com moradia, gastos totais com educação e gastos totais com
# transporte, faça um diagnóstico da saúde financeira do usuário, com base nos
# valores percentuais acima expostos, informando qual é o percentual da renda
# mensal total comprometido por cada custo.

# código também disponível em:
# https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/introducao-logica/AT/03-analise-renda-mensal.py

categorias = [
    {'tipo': 'Moradia', 'porcentagem_maxima': 30},
    {'tipo': 'Educação', 'porcentagem_maxima': 20},
    {'tipo': 'Transporte', 'porcentagem_maxima': 15},
]

def calculo_gasto_mensal(renda_mensal, tipo, limite_gastos, gastos):
    renda_mensal = float(renda_mensal + '.0')
    limite_gastos = float(limite_gastos)
    gastos = float(gastos)

    percentual_gasto = round(gastos / renda_mensal * 100, 2)
    valor_limite = round(limite_gastos * renda_mensal / 100, 2)

    if(percentual_gasto > limite_gastos):
        status_gasto = f"Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_limite}."
    else:
        status_gasto = 'Seus gastos estão dentro da margem recomendada.'

    return f"Seus gastos totais com {tipo} comprometem {percentual_gasto}% de sua renda total. O máximo recomendado é de {limite_gastos}%. {status_gasto} \n"

while True:
    # Pergunta e valida a renda mensal
    renda_mensal = input("Renda Mensal: R$ ")

    if(not renda_mensal.replace(',', '').replace('.', '').isnumeric() or float(renda_mensal) <= 0):
        print("A renda informada é inválida.")
    else:
        break

diagnostico = "\nDiagnóstico: \n\n"
for categoria in categorias:
    while True:
        # Pergunta e valida os gastos
        gasto = input(f"Gastos totais com {categoria['tipo']}: R$ ") or '0'

        if(not gasto.replace(',', '').replace('.', '').isnumeric()):
            print("O valor informado é inválido.")
        else:
            diagnostico += calculo_gasto_mensal(renda_mensal, categoria['tipo'], categoria['porcentagem_maxima'], gasto)
            break

print(diagnostico)

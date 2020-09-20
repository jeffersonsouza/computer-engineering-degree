# ENUNCIADO:
# Desenvolva um programa contendo uma função que liste, por país, a estimativa de variação do PIB,
# em percentual, entre 2013 e 2020.
#
# código também disponível em:
# https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/introducao-logica/AT/05_b-revisao-pib.py

arquivo = open('assessment-pibs.csv', 'r')
paises_pibs = arquivo.read()
paises_pibs = paises_pibs.splitlines()
arquivo.close() # já que não vou mais precisar ler o arquivo, ele pode ser fechado logo aqui

def calcula_diferenca_pib(valor_inicial, valor_final):
    valor_inicial, valor_final = float(valor_inicial), float(valor_final)
    return round(((valor_final - valor_inicial) / valor_inicial) * 100, 2)

def retorna_variacao_pib():
    for pais_pib in paises_pibs[1:]:
        pais_pib = pais_pib.split(',')
        print(f"{pais_pib[0]:18}\t Variação de {calcula_diferenca_pib(pais_pib[1], pais_pib[len(pais_pib) - 1])}% entre 2013 e 2020.")

retorna_variacao_pib()

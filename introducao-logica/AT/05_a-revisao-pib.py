# ENUNCIADO:
# Desenvolva um programa contendo uma função que permita ao usuário solicitar o PIB de um país para
# um determinado ano.
# O programa solicita ao usuário o nome do país e o ano desejado.
# Caso o país solicitado ou o ano não sejam válidos, o programa deve informar, na saída, a mensagem:
# `País não disponível.` ou `Ano não disponível.` a depender do tipo de dado não encontrado.
#
# código também disponível em:
# https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/introducao-logica/AT/05_a-revisao-pib.py

campos = [
    {'label': 'Informe um país:', 'valor': 0},
    {'label': 'Informe um ano entre 2013 e 2020:', 'valor': 0},
]

arquivo = open('assessment-pibs.csv', 'r')
paises_pibs = arquivo.read()
paises_pibs = paises_pibs.splitlines()
arquivo.close() # já que não vou mais precisar ler o arquivo, ele pode ser fechado logo aqui

def retorna_pib(pais, ano):
    ano = str(ano)

    cabecalho = paises_pibs[0].split(',')
    if(ano in cabecalho):
        ano_index = cabecalho.index(ano)
    else:
        print('Ano não disponível')
        return

    for pais_pib in paises_pibs:
        pais_pib = pais_pib.split(',')
        if(pais_pib[0].lower() == pais.lower()):
            print(f"PIB {pais_pib[0]} em {ano}: US${pais_pib[ano_index]} trilhões.")
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

retorna_pib(campos[0]['valor'], campos[1]['valor'])

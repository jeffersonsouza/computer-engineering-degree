# Faça uma funçãoum programa em Python que simula um lançamento de dados.
# Lance o dado 100 vezes e armazene os resultados em um vetor.
# Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores (1-6) e uma função do módulo 'random' de Python
# para gerar números aleatórios, simulando os lançamentos dos dados. (código)
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/TP3/
import random

rolagens = 100
resultados = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0
}

def rolar_dado(rolagens):
    for n in range(0, rolagens):
        resultado = random.randint(1, 6)

        resultados[f"{resultado}"] += 1

    for lado in resultados:
        print(f"O número {lado} teve {resultados[lado]} ocorrência{'s' if resultados[lado] > 1 else ''}.")

rolar_dado(rolagens)

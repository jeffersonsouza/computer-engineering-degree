# Escreva um programa em Python que leia diversas frases até a palavra “Sair” ser digitada.
# Indique quais frases apresentam a palavra “eu”
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/TP3/

import re

frases = []

executando = True
while executando:
    while True:
        data = input(f"Informe uma palavra: ")

        if data == 'sair':
            executando = False
            break

        if not data:
            print(f"O valor informado é inválido")
        else:
            frases.append(data)
            break

for frase in frases:
    if bool(re.search(r'\beu\b', frase.lower())):
        print(f"A frase \"{frase}\" possui a sentença \"eu\"")

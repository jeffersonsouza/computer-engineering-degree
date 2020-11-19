# Escreva um programa em Python que leia um vetor de 10 palavras e mostre-as na ordem inversa de leitura
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/TP3/

palavras = []
for i in range(1, 11):

    while True:
        data = input(f"Informe uma palavra: ")

        if not data:
            print(f"O valor informado é inválido")
        else:
            palavras.append(data)
            break

for palavra in palavras:
    print(palavra[::-1])

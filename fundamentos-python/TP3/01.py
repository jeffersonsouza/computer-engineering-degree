# Usando Python, faça o que se pede (código e printscreen):
#  - Crie uma lista vazia;
#  - Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
#  - Imprima a lista;
#  - Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
#  - Imprima a lista modificada;
#  - Imprima também o tamanho da lista usando a função len();
#  - Altere o valor do último elemento para 6 e imprima a lista modificada.
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/TP3/

# item "a"
lista = []

# item "b"
for n in range(1, 6):
    lista.append(n)

# item "c"
print(lista)

# item "d"
for n in [3, 6]:
    if n in lista:
        lista.remove(n)

# itens "e" e "f"
print(lista, '-> Tamanho:', len(lista), 'itens')

# item "g"
lista[-1] = 6
print(lista)

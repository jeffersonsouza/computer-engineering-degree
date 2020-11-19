# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/fundamentos-python/TP1
# # Dada uma tupla e um elemento, elimine esse elemento da tupla.

def remove_tupla(tupla, elemento):
    if elemento in tupla:
        lista = list(tupla)
        lista.remove(elemento)

        print(tuple(lista))


dias_semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
remove_tupla(dias_semana, 'terça')

# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/fundamentos-python/TP1
# Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.

def divide_tupla(tupla):
    corte = round(len(tupla) / 2)
    print(tupla[:corte], "\n", tupla[corte:])

dias_semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
divide_tupla(dias_semana)

# Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.

def inverte_tupla(tupla):
    lista = list(tupla)[::-1]

    print(tuple(lista))

dias_semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
inverte_tupla(dias_semana)

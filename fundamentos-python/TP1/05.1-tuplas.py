# Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o indice do mesmo

def retorna_indice(tupla, elemento):
    if elemento in tupla:
        return tupla.index(elemento)

    return 'O elemento informado não existe na tupla'

dias_semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
print(retorna_indice(dias_semana, 'segunda'))

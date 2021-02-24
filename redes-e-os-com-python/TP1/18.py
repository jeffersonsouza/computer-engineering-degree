# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import psutil

try:
    memory = round(psutil.virtual_memory().total/(1024*1024*1024), 2)
    swap = round(psutil.swap_memory().total/(1024*1024*1024), 2)
    print(f"O sistema tem {memory}Gb de memória principal.")
    print(f"O sistema tem {swap}Gb de memória swap.")
except:
    print('Houve um erro ao obter os dados do sistema.')

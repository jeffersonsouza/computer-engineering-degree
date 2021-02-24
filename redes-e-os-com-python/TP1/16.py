# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import psutil

try:
    cpu_times = psutil.cpu_times(percpu=True)
    print(f"{cpu_times}")
except:
    print('Houve um erro ao obter os dados do sistema.')

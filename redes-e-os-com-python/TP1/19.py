# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import psutil

try:
    partitions = psutil.disk_partitions()
    hard_drive = psutil.disk_usage(partitions[0].mountpoint)

    print(f"A partição principal tem cerca de {round(hard_drive.free / (1024*1024*1024), 2)}Gb de espaço disponível.")
except:
    print('Houve um erro ao obter os dados do sistema.')

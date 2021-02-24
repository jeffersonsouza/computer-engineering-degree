# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import psutil, os

try:
    partitions = psutil.disk_partitions(all=True)
    current_partition = None
    current_path = os.getcwd()
    hard_drive = psutil.disk_usage(current_path)

    for partition in partitions:
        if partition.mountpoint != '/' and partition.mountpoint in current_path:
            current_partition = partition

    if current_partition is None:
        current_partition = partitions[0]

    print(f"A partição atual tem cerca é '{current_partition.mountpoint}', "
          f"com o sistema de arquivos '{current_partition.fstype}', "
          f"{round(hard_drive.total / (1024*1024*1024), 2)}Gb de espaço total "
          f"e {round(hard_drive.free / (1024*1024*1024), 2)}Gb de espaço disponível.")
except:
    print('Houve um erro ao obter os dados do sistema.')

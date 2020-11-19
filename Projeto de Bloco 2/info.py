import psutil, platform

def get_virtual_memory():
    memory = psutil.virtual_memory()
    capacity = round(memory.total/(1024*1024*1024), 2)


    print('Capacidade total de Memória:', capacity, 'GB')

get_virtual_memory()

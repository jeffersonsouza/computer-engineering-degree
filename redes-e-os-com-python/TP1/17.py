# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import psutil, time

try:
    for i in range(1, 20):
        cpu_usage = psutil.cpu_percent()
        print(f"Uso atual de CPU {cpu_usage}%")
        time.sleep(1)
except:
    print('Houve um erro ao obter os dados do sistema.')

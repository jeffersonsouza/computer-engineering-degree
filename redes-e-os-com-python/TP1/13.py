# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import subprocess

try:
    process = subprocess.Popen(['echo', 'Novo processo criado =]'])

    print(f"Processo criado com o PID {process.pid}")
except:
    print('Houve um erro ao executar o processo')

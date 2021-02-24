# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import os

path = '.'
files = os.listdir(path)

for file in files:
    if os.path.isfile(os.path.join(path, file)):
        details = os.stat(os.path.join(path, file))
        print(f"O arquivo {file} possui {round(details.st_size / 1024, 2)}Kb;")
    else:
        print(f"O caminho especificado não existe")

# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import os

filename = '01.py'
path = '.'
fullpath = os.path.join(path, filename)

if os.path.exists(fullpath) and os.path.isfile(fullpath):
    print(f"A extensão do arquivo é {os.path.splitext(fullpath)[1]}")
else:
    print(f"O caminho ou arquivo especificado não existe")

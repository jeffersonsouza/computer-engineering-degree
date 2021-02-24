# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import os

filename = '01.py'
path = '.'
fullpath = os.path.join(path, filename)

if os.path.exists(fullpath):
    print(f"O caminho especificado existe.")
    print('O caminho especificado é um arquivo.') if os.path.isfile(fullpath) else None
else:
    print(f"O caminho especificado não existe")

# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import os

while True:
    path = input(f"Indique o caminho completo para o arquivo que quer abrir: ") or 0

    if not path:
        print("O valor informado é inválido.")
    else:
        break

if os.path.exists(path) and os.path.isfile(path):
    print(f"Abrindo arquivo '{path}'...")
    try:
        os.execl(os.environ['SYSTEMROOT'] + '\\System32\\notepad.exe', path)
    except:
        print('Houve um erro ao executar o processo "Notepad"')
else:
    print(f"O caminho ou arquivo especificado não existe")

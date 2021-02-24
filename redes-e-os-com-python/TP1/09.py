# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import os
from datetime import datetime, timezone

path = '.'
files = os.listdir(path)

for file in files:
    if os.path.isfile(os.path.join(path, file)):
        details = os.stat(os.path.join(path, file))
        created_at = datetime.fromtimestamp(details.st_atime, tz=timezone.utc).strftime('%d/%m/%Y %H:%M')
        updated_at = datetime.fromtimestamp(details.st_mtime, tz=timezone.utc).strftime('%d/%m/%Y %H:%M')
        print(f"O arquivo {file} foi criado em {created_at} e a data da última alteração é {updated_at};")
    else:
        print(f"O caminho especificado não existe")

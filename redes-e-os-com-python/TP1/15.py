# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import psutil
from datetime import datetime, timezone

while True:
    pid = input(f"Informe o número do processo que você deseja informações sobre: ") or 0

    if not pid.isnumeric():
        print("O valor informado é inválido.")
    else:
        break

if psutil.pid_exists(int(pid)):
    try:
        process = psutil.Process(int(pid))
        created_date = datetime.fromtimestamp(process.create_time(), tz=timezone.utc).strftime('%d/%m/%Y %H:%M')

        print(f"O processo #{pid} criado pelo usuário {process.username()} em {created_date}UTC está consumindo atualmente {process.memory_info().rss // 1024}Kb de memória.")
    except:
        print('Houve um erro ao obter os dados do processo')
else:
    print(f"O processo informado não existe")

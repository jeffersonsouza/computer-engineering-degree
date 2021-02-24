# Disponível em https://github.com/jeffersonsouza/computer-engineering-degree/tree/master/redes-e-os-com-python/TP1

import os

print(f"PID do processo: {os.getpid()}")

print(f"Grupo de usuário do processo: {os.getgid()}") if os.getgid() else None

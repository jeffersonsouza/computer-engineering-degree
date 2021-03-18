import socket
import psutil

def formatar_info_texto(cpu_percent, mem_percent):
    return '{:>8.2f}'.format(cpu_percent) + '{:>8.2f}'.format(mem_percent)

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtém o nome da máquina
host = socket.gethostname()
porta = 9006

# Associa a porta
socket_servidor.bind((socket.gethostname(), porta))
# Escutando...
socket_servidor.listen()

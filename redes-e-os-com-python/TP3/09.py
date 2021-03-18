import socket
import psutil, os

# configs
host = socket.gethostname()
port = 9991

# create a socket instance and set the host and port
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))

# listen for connections...
print("Server ", host, " listening on port ", port)

while True:
    (msg, client) = server.recvfrom(1024)
    if msg.decode('ascii') == 'fim':
        break
    current_path = os.getcwd()
    hard_drive = psutil.disk_usage(current_path)
    server.sendto(f"Total: {round(hard_drive.total / (1024*1024*1024), 2)}Gb\nDisponivel: {round(hard_drive.free / (1024*1024*1024), 2)}Gb".encode('ascii'), client)

server.close()
print('exiting...')

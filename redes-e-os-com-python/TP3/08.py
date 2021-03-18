import socket

# configs
host = socket.gethostname()
port = 9991

# create a socket instance and set the host and port
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    client.sendto(b'data', (host, port))
    info_bytes = client.recv(1024)
    print(info_bytes.decode('ascii'))
    client.sendto(b'fim', (host, port))
except Exception as erro:
    print(str(erro))

client.close()

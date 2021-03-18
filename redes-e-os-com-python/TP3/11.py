import socket
import os

# configs
host = socket.gethostname()
port = 8881
print(host)

def get_file_size(file):
    if os.path.isfile(os.path.join('.', file)):
        details = os.stat(os.path.join('.', file))

        return f"{round(details.st_size / 1024, 2)}"

    return '-1'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # create a socket instance and set the host and port
    server.bind((host, port))
    # listen for connections...
    server.listen()
    print("Server ", host, " listening on port ", port)

    (client, addr) = server.accept()

    while True:
        msg = client.recv(1024)

        file_name = msg.decode('utf-8')
        if file_name:
            client.send(get_file_size(file_name).encode('utf-8'))

except Exception as erro:
    print(str(erro))
    server.close()


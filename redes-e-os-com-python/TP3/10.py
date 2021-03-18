import socket

# configs
host = socket.gethostname()
port = 8881
file = '12.py'

# create a socket instance and set the host and port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

try:
    client.send(file.encode('utf-8'))
    info_bytes = client.recv(1024)
    file_size = info_bytes.decode('utf-8')
    if file_size != '-1':
        print(f"The file '{file}' has {file_size}kb")
    else:
        print(f"The file '{file}' could not be found.")

    client.close()

except Exception as erro:
    print(str(erro))


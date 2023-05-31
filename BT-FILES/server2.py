import os
import socket
import struct

# Función para manejar la transferencia de archivos desde el cliente al servidor
def receive_file(client):
    # Se recibe el nombre del archivo a guardar en el servidor
    file_name = client.recv(1024).decode()
    file_size = int(client.recv(1024).decode())

    # Se crea un nuevo archivo en el servidor para escribir los datos recibidos
    with open(file_name, 'wb') as file:
        received_size = 0
        while received_size < file_size:
            # Se recibe la longitud del fragmento
            chunk_size = struct.unpack('Q', client.recv(struct.calcsize('Q')))[0]
            chunk_data = b''
            while len(chunk_data) < chunk_size:
                # Se reciben los datos del fragmento
                remaining_size = chunk_size - len(chunk_data)
                chunk_data += client.recv(remaining_size)
            file.write(chunk_data)
            received_size += len(chunk_data)

    print(f"File '{file_name}' received and saved.")

# Configuración del servidor Bluetooth
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind(("e8:d0:fc:fe:12:9e", 4))
server.listen(1)

print("Waiting for connection...")

client, addr = server.accept()
print(f"Accepted connection from {addr}")

try:
    while True:
        data = client.recv(1024).decode('utf-8')
        if not data:
            break

        if data == "!send_file":
            # Se recibe el comando "!send_file" del cliente
            receive_file(client)
            continue

        print(f"Received: {data}")
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))

except OSError:
    pass

print("Disconnected")

client.close()
server.close()

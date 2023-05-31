import os
import socket
import struct

# Función para manejar la transferencia de archivos desde el cliente al servidor
def receive_file(client):
    # Se recibe el nombre del archivo a guardar en el servidor
    file_name = client.recv(1024).decode()
    file_size = int(client.recv(1024).decode())

    # Se crea un nuevo archivo en el cliente para escribir los datos recibidos
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

# Configuración del cliente Bluetooth
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("e8:d0:fc:fe:12:9e", 4))

try:
    while True:
        choice = input("Enter 'm' to send a message, 'f' to send a file, or 'q' to quit: ")
        if choice == 'q':
            break

        if choice == 'm':
            message = input("Enter message: ")
            client.send(message.encode('utf-8'))

            # Se espera la respuesta del servidor
            response = client.recv(1024).decode('utf-8')
            print(f"Received: {response}")

        elif choice == 'f':
            # Se envía el comando "!send_file" al servidor
            client.send("!send_file".encode('utf-8'))
            file_path = input("Enter file path: ")  # Ruta del archivo a enviar
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            # Se envía el nombre del archivo y su tamaño al servidor
            client.send(file_name.encode('utf-8'))
            client.send(str(file_size).encode('utf-8'))
            # Se lee el archivo y se envían fragmentos de datos al servidor
            with open(file_path, 'rb') as file:
                chunk_size = 1024  
                while True:
                    chunk_data = file.read(chunk_size)
                    if not chunk_data:
                        break
                    # Se envía la longitud del fragmento al servidor
                    client.send(struct.pack('Q', len(chunk_data)))
                    # Se envían los datos del fragmento al servidor
                    client.sendall(chunk_data)

            print(f"File '{file_name}' sent.")

except KeyboardInterrupt:
    pass

print("Disconnected")

client.close()

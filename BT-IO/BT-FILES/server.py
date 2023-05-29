import os
import socket

# Función para enviar archivos
def send_file(client_socket, file_path):
    # Abre el archivo en modo lectura binaria
    with open(file_path, "rb") as file:
        # Obtiene el tamaño del archivo
        file_size = os.path.getsize(file_path)

        # Envía el nombre del archivo de destino y el tamaño al cliente
        client_socket.send(file_path.encode())
        client_socket.send(str(file_size).encode())

        # Lee y envía los datos del archivo en bloques
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.sendall(data)

        # Envía una marca de finalización
        client_socket.send(b"<END>")

# Dirección y puerto para el servidor
HOST = "e8:d0:fc:fe:12:9e"
PORT = 4

# Crea el socket del servidor
server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Vincula el socket del servidor a la dirección y puerto
server_socket.bind((HOST, PORT))

# Escucha por conexiones entrantes
server_socket.listen()

print("Waiting for incoming connections...")

# Acepta una conexión entrante
client_socket, client_address = server_socket.accept()

print(f"Connected to {client_address}")

try:
    while True:
        # Recibe los datos del cliente
        data = client_socket.recv(1024).decode()

        # Si no se reciben datos, se sale del bucle
        if not data:
            break

        # Si el mensaje recibido es "file", solicita el archivo al cliente y lo envía
        if data == "file":
            # Recibe el nombre del archivo del cliente
            file_name = client_socket.recv(1024).decode()
            print(f"Receiving file: {file_name}")

            # Recibe el tamaño del archivo del cliente
            file_size = int(client_socket.recv(1024).decode())

            # Lee y guarda los datos del archivo en bloques
            received_data = b""
            while len(received_data) < file_size:
                data = client_socket.recv(1024)
                received_data += data

            # Guarda el archivo recibido
            with open(file_name, "wb") as file:
                file.write(received_data)

            print(f"File received: {file_name}")

        else:
            # Imprime el mensaje recibido del cliente
            print(f"Received: {data}")

            # Solicita al usuario que ingrese una respuesta
            message = input("Enter message: ")

            # Envía la respuesta al cliente
            client_socket.send(message.encode())

except OSError:
    pass

# Cierra la conexión y el socket del cliente
client_socket.close()

# Cierra el socket del servidor
server_socket.close()

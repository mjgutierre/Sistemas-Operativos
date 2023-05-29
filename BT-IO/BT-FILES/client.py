import socket
import os
import tqdm

# Función para manejar la transferencia de archivos desde el cliente al servidor
def receive_file(client):
    # Se recibe el nombre del archivo a guardar en el servidor
    file_name = client.recv(1024).decode()
    print("Receiving file:", file_name)
    file_size = int(client.recv(1024).decode())

    # Se crea un nuevo archivo en el servidor para escribir los datos recibidos
    with open(file_name, 'wb') as file:
        received_size = 0
        progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1024, total=file_size, desc=file_name)
        while received_size < file_size:
            data = client.recv(1024)
            file.write(data)
            received_size += len(data)
            progress.update(len(data))
        progress.close()

    print(f"File '{file_name}' received and saved.")

# Configuración del cliente Bluetooth
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("e8:d0:fc:fe:12:9e", 4))

print(f"Connected!")

try:
    while True:
        # Solicitar al usuario si desea enviar un mensaje o un archivo
        choice = input("Enter 'm' to send a message, 'f' to send a file, or 'q' to quit: ")

        if choice == "m":
            # Enviar mensaje
            message = input("Enter message: ")
            client.send(message.encode('utf-8'))
            data = client.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")

        elif choice == "f":
            # Enviar archivo
            file_path = input("Enter file path: ")
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)

            # Enviar el comando especial para indicar al servidor que se enviará un archivo
            client.send("!send_file".encode())

            # Enviar el nombre y el tamaño del archivo al servidor
            client.send(file_name.encode())
            client.send(str(file_size).encode())

            # Abrir el archivo y enviar los datos en bloques
            with open(file_path, "rb") as file:
                for _ in tqdm.tqdm(range(file_size // 1024 + 1), unit="B", unit_scale=True, unit_divisor=1024, desc=file_name):
                    data = file.read(1024)
                    if not data:
                        break
                    client.send(data)

            # Enviar la marca de finalización "<END>"
            client.send(b"<END>")

            print(f"File '{file_name}' sent.")

        elif choice == "q":
            break

except OSError:
    pass

print("Disconnected")

client.close()

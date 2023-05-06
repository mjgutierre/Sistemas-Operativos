#codigo edison
import bluetooth

def start_server():
    print('Inicia el servidor')
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 3
    server_sock.bind(("00:E9:3A:91:75:80", port))
    server_sock.listen(1)
    print(f"Servidor de Bluetooth iniciado en el puerto {port}")
    client_sock, client_info = server_sock.accept()
    print(f"Conexión entrante de {client_info}")
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        print(f"Mensaje recibido de {client_info}: {data.decode()}")
        message = input("Ingrese un mensaje: ")
        client_sock.send(message.encode())
    print(f"Conexión cerrada con {client_info}")
    client_sock.close()
    server_sock.close()

if __name__ == '__main__':
    start_server()

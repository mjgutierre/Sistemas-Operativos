#cliente edison
import bluetooth
import threading

def receive_message(sock):
    print('Habilitado para escuchar....')
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(f"Mensaje recibido: {data.decode()}")

def start_client():
    try:
        client_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_address = input("Ingrese la dirección MAC del servidor: ")
        port = int(input("Ingrese el puerto de conexión: "))
        client_sock.connect((server_address, port))
        print(f"Conectado al servidor en {server_address}")
    
        receive_thread = threading.Thread(target=receive_message, args=(client_sock,))
        receive_thread.start()

        while True:
            message = input("Ingrese un mensaje: ")
            client_sock.send(message.encode())
        
    except OSError as errorServidor:
        print("Parece que algo salio mal con el servidor. Revisa la dirección y el estado del servidor")
        print(f">>> Error: {errorServidor}")
    except:
        print("Parece que algo salio mal con el programa")
    finally:
        client_sock.close()


if __name__ == '__main__':
    start_client()

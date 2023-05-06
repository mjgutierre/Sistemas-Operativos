#nueva implementacion
import bluetooth
import threading
import PySimpleGUI as sg

# create Bluetooth server
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

# create GUI window
def create_window():
    sg.theme('DarkAmber')
    layout = [[sg.Text('Bluetooth Chat')],
              [sg.Text('Introduzca el mensaje a enviar'), sg.InputText(key='input')],
              [sg.Button('Enviar'), sg.Button('Salir')]]
    window = sg.Window('Bluetooth Chat', layout)
    return window

# create threads to run server and GUI in parallel
def start_threads():
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    gui_thread = threading.Thread(target=start_gui)
    gui_thread.start()

# run the GUI
def start_gui():
    window = create_window()
    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == 'Salir':
            break
        if event == 'Enviar':
            message = values['input']
            # send message over Bluetooth
            # ...

    window.close()

if __name__ == '__main__':
    start_threads()

import socket
import threading
import bluetooth
import PySimpleGUI as sg


# Connection Data
host = "e8:d0:fc:fe:12:9e"
port = 4


# GUI Layout
layout = [
    [sg.Multiline(size=(60, 20), key="-OUTPUT-", disabled=True)],
    [sg.InputText(key="-MESSAGE-"), sg.Button("Send"), sg.Button("Exit")]
]

# Create the Window
window = sg.Window("Bluetooth Chat Server", layout)


# Starting Server
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)#bluetooth.BluetoothSocket(bluetooth.RFCOMM)#
server.bind((host, port))#socket de tipo bluetooth bindin a la mac address de nuestro dispositivo 
server.listen()
print(f"Servidor de Bluetooth iniciado en el puerto {port}")

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            data = clients.data(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[data]
            broadcast('{} left the chat!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


# Event Loop to process "Exit" button and send messages
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Send":
        message = f"{values['-MESSAGE-']}\n"
        broadcast(message.encode('ascii'))
        window['-OUTPUT-'].update(f"You: {message}")
        window['-MESSAGE-'].update("")

print("server is listening")
receive()

server.close()
window.close()



import socket
import threading
import PySimpleGUI as sg

# Layout
layout = [
    [sg.Text("Nickname:"), sg.Input(key="nickname")],
    [sg.Multiline(size=(60, 20), key="output")],
    [sg.InputText("", key="input"), sg.Button("Send"), sg.Button("Disconnect")]
]

# Window
window = sg.Window("Bluetooth Chat Client", layout)


# Choosing Nickname
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if values["nickname"]:
        nickname = values["nickname"]
        break

# Connecting To Server
#client = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
#client= bluetooth.BluetoothSocket(bluetooth.RFCOMM)
direccion=("e8:d0:fc:fe:12:9e", 1)
client.connect(direccion)
print(f"Connected!")


# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                window["output"].print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Disconnect":
            client.send("Disconnect".encode('ascii'))
            break
        elif event == "Send":
            message = '{}: {}'.format(nickname, values["input"])
            client.send(message.encode('ascii'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive(), args=(client,))#,))
receive_thread.start()

write_thread = threading.Thread(target=write())
write_thread.start()

# Close Window and Connection When Done
write_thread.join()
client.close()
window.close()
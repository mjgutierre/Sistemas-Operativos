import socket
import tkinter as tk
from threading import Thread


def receive_messages():
    while True:
        try:
            data = client.recv(1024)
            if data:
                message_list.insert(tk.END, data.decode('utf-8'))
        except OSError:
            break


def send_message():
    message = input_box.get()
    if message:
        client.send(message.encode('utf-8'))
        input_box.delete(0, tk.END)


def close_connection():
    client.close()
    root.quit()


# Create the GUI window
root = tk.Tk()
root.title("Bluetooth Chat Client")

# Create the message list
message_list = tk.Listbox(root, height=15, width=50)
message_list.pack()

# Create the input box and send button
input_box = tk.Entry(root, width=50)
input_box.pack()
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Create the close button
close_button = tk.Button(root, text="Close", command=close_connection)
close_button.pack()

# Set up the Bluetooth connection
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("e8:d0:fc:fe:12:9e", 4))

# Start receiving messages in a separate thread
receive_thread = Thread(target=receive_messages)
receive_thread.start()

# Start the GUI main loop
root.mainloop()

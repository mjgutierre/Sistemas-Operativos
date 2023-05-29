import os 
import socket
 
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("e8:d0:fc:fe:12:9e",4))

print(f"Connected!")

file = open ("image.png","rb")
file_size = os.path.getsize("image.png")

client.send("received_image.png".encode())
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)
client.send(b"<END>")

file.close()
client.close()

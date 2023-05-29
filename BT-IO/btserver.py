import socket

#protocolo RFCOMM
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)  # RFCOMM specific protocol
server.bind(("e8:d0:fc:fe:12:9e", 4))  # MAC Address and Channel 4
server.listen(1)

print("Waiting for connection...")

client, addr = server.accept()
print(f"Accepted connection from {addr}")

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode('utf-8')}")
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
except OSError:
    pass

print("Disconnected")

client.close()
server.close()



import bluetooth

# Especifica la dirección MAC del servidor Bluetooth
hostMACAddress = 'e8:d0:fc:fe:12:9e'

# Busca los servicios disponibles en el servidor Bluetooth
services = bluetooth.find_service(address=hostMACAddress)

# Imprime la información de dirección de cada servicio
for service in services:
    print(f"Service Name: {service['name']}")
    print(f"Host: {service['host']}")
    print(f"Port: {service['port']}")
    print(f"Description: {service['description']}")
    print(f"Protocol: {service['protocol']}")
    print(f"Service Classes: {service['service-classes']}")
    print(f"Profiles: {service['profiles']}")
    print("")

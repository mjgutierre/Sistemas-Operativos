import bluetooth

# Busca dispositivos Bluetooth cercanos
nearby_devices = bluetooth.discover_devices()

# Imprime los dispositivos encontrados
print('============== [DISPOSITIVOS BLUETOOTH] ===============')
i = 1
for bdaddr in nearby_devices:
    print(f' [{i}] _-{bluetooth.lookup_name(bdaddr)}_-  [ {bdaddr} ]')
    i+=1

# Establece la dirección MAC del dispositivo al que te quieres conectar
bd_addr = "e8:d0:fc:fe:12:9e" #"D4:63:DE:45:45:10"
port = 1 # Establece el puerto serial utilizado para la conexión Bluetooth
print(f' .... Puerto establecido: {bd_addr} ==> port:{port}')
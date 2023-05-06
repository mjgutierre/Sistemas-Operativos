#bt edison
import bluetooth

# Busca dispositivos Bluetooth cercanos
nearby_devices = bluetooth.discover_devices()

# Imprime los dispositivos encontrados
print('=== [DISPOSITIVOS BLUETOOTH] ===============')
i = 1
for bdaddr in nearby_devices:
    print(f' [{i}] _-{bluetooth.lookup_name(bdaddr)}_-  [ {bdaddr} ]')
    i+=1

# Establece la dirección MAC del dispositivo al que te quieres conectar
#bd_addr = "00:00:00:00:00:00"  # Reemplaza con la dirección MAC de tu dispositivo Bluetooth
bd_addr = "D4:63:DE:45:45:10"

# Establece el puerto serial utilizado para la conexión Bluetooth
port = 1
print(f' .... Puerto establecido: {bd_addr} ==> port:{port}')

'''
# Establece la conexión Bluetooth
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

# Envía un mensaje al dispositivo Bluetooth conectado
sock.send("¡Hola desde Python!")

# Cierra la conexión Bluetooth
sock.close()
'''
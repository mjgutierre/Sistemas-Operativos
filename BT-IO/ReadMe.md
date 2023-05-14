# Informacion de la asignatura 
Sistemas Operativos 

## Datos de los estudiantes 
Paulina Ocampo Duque ***mpocampod@eafit.edu.co***

Juan Jose Sanchez Cortes ***jjsanchezc@eafit.edu.co***

Maria José Gutiérrez Estrada. ***mjgutierre@eafit.edu.co***

# Práctica de puertos IO

En la asignatura de Sistemas Operativos, se realizará una práctica en la que se evaluará el uso de la Entrada y la Salida de la computadora (IO), mediante la creación de un programa Cliente/Servidor para un chat de texto. En este proyecto se utilizarán los puertos Bluetooth y los sockets por TCP/IP.

Los objetivos específicos de esta práctica son:

- Diseñar e implementar un programa Cliente/Servidor para un chat de texto.
- Utilizar los puertos Bluetooth y los sockets por TCP/IP para la comunicación entre el Cliente y el Servidor.
- Evaluar el uso de la Entrada y la Salida de la computadora (IO) en la implementación del programa.
- Presentar un informe oral que explique el diseño y la forma de uso del programa desarrollado.

## Guia de Uso

Procedemos a activar un entorno virtual o instalar los requerimientos desde nuestra consola en la maquina local.

- Para activar el entorno virtual podemos ejecutar en la carpeta el siguiente comando:

      .\Scripts\activate 
    
- O instalar los requerimientos del txt podemos correr el siguiente comando:

      pip install requirements.txt

Entramos a la carpeta donde se encuentran los archivos 

    cd BT-IO

### Servidor

    py btserver.py
  
  
### Cliente
  
    py btclient.py
    
    
    
## Referencias

- [Bluetooth socket Programming](https://roboticsknowledgebase.com/wiki/networking/bluetooth-sockets/#bluetooth-socket-programming-using-bash)
- [PyBluez Documentation](https://pybluez.readthedocs.io/en/latest/api/discover_devices.html)
- [Bluetooth Chat](https://github.com/NeuralNine/youtube-tutorials/tree/main/Bluetooth%20Chat)

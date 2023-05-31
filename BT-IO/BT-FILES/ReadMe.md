# Informacion de la asignatura 
Sistemas Operativos 

#   Práctica Final - Sistemas Operativos

## Datos de los estudiantes 
Paulina Ocampo Duque ***mpocampod@eafit.edu.co***

Juan Jose Sanchez Cortes ***jjsanchezc@eafit.edu.co***

Maria José Gutiérrez Estrada. ***mjgutierre@eafit.edu.co***

## Objetivo:
El objetivo de esta práctica final es diseñar e implementar un programa que permita la transmisión de una fuente de imagen o sonido desde un punto A a un punto B, utilizando un modelo cliente-servidor y el manejo de conceptos de concurrencia con multiprocesos.

## Requerimientos:
- El programa deberá ser capaz de capturar la fuente de imagen o sonido en el punto A, codificar y transmitirla a través de un socket IP utilizando tramas de tamaño de 250 KB.
- Para mejorar la eficiencia del programa, se deberá implementar el manejo de conceptos de concurrencia con multiprocesos para que la captura, codificación y transmisión de la información puedan ser ejecutadas de forma simultánea.
- En el punto B, el programa deberá recibir las tramas de datos, decodificarlas y reconstruir la imagen o el sonido original.
- También se deberá implementar el manejo de conceptos de concurrencia con multiprocesos en el punto B para mejorar la eficiencia del programa en la recepción, decodificación y reconstrucción de la información.
- Se espera que los estudiantes implementen medidas de seguridad y control de errores para garantizar la integridad de la información transmitida.
- Se recomienda implementar técnicas de compresión de datos para reducir el tamaño de las tramas y mejorar la eficiencia de la transmisión.
- La interfaz gráfica de usuario es opcional, pero se recomienda su implementación para facilitar el uso del programa.
- La interfaz gráfica deberá permitir la selección de la fuente de imagen o sonido a transmitir, la configuración de los parámetros de transmisión (como la dirección IP y el puerto de destino) y la visualización del progreso de la transmisión.
- Se deberá mostrar el resultado final de la imagen o el sonido transmitido, asegurándose de que la información haya sido transmitida en su totalidad y se haya generado de forma correcta.


## Documentacion Tecnica

Como ejecutar?

    pip install requirements.txt

Recordar que para efectos de nuestro codigo se debera cambiar las siguientes lineas en el servidor y cliente para que pueda ser efectiva la conexion.   

    
En un dispositivo ejectuar
   
      py servidor2.py      

En otro dispositivo ejecutar
    
      py cliente1.py

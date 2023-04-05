
## Informacion de la asignatura 
Sistemas Operativos 

## Datos de los estudiantes 
Paulina Ocampo Duque ***mpocampod@eafit.edu.co***

Juan Jose Sanchez Cortes ***jjsanchez@eafit.edu.co***

Maria José Gutiérrez Estrada. ***mjgutierre@eafit.edu.co***

## Tabla de contenido 
1. [Objetivo](https://github.com/mjgutierre/Sistemas-Operativos#objetivo)
2. [Parte 1: Descripción Programa Backup](https://github.com/mjgutierre/Sistemas-Operativos/blob/master/ReadMe.md#parte-1-descripción-programa-backup)
3. [Parte 1. Descripción Técnica](https://github.com/mjgutierre/Sistemas-Operativos#uso)
4. [Parte 2. Descripción Programa Restauración](https://github.com/mjgutierre/Sistemas-Operativos#parte-2-crear-el-programa-de-restauración)
5. [Parte 2. Descripción Técnica]

# Objetivo
El objetivo de esta práctica evaluable es crear un programa que permita realizar una copia de seguridad de una carpeta en fragmentos de 512 MB, y otro programa que permita restaurar la copia de seguridad a su estado original. El programa debe ser capaz de trabajar con archivos de cualquier tamaño.

## Parte 1: Descripción Programa Backup

Crear el programa de copia de seguridad
El programa de copia de seguridad cuenta con los siguientes requerimientos de diseño:

- Recibe como entrada la ruta de la carpeta que se desea copiar (source_folder) y la ruta de la carpeta donde se guardarán los fragmentos de la copia de seguridad (destination_folder).
- Divide los archivos de la carpeta fuente en varios fragmentos (chunks) de tamaño máximo de 512 MB, y los guarda en la carpeta de la copia de seguridad.
- Nombra los fragmentos de la copia de seguridad de forma que se pueda identificar fácilmente a qué carpeta pertenecen y en qué orden deben ser restaurados.
- Imprime un mensaje indicando que la copia de seguridad se ha completado con éxito.
- Crea un archivo en formato JSON en la carpeta destino con la composición del archivo backup, es decir, con los archivos respaldados, sus tamaño y cuantos archivos de 512 MB ser crearon.

### USO

Para usar este programa de copia de seguridad, se necesitará especificar la ruta de la carpeta fuente y de la carpeta destino.

Ejemplo 

        source_folder = "C:/Users/USER/Downloads/FotosImportantes"
        destination_folder = "D:/Backup"


Al estar dentro de la carpeta procedemos a crear un entorno virtual o instalar los requerimientos desde nuestra consola en la maquina local.

- Para activar el entorno virtual podemos ejecutar en la carpeta el siguiente comando:

        .\Scripts\activate 

- Para instalar los requerimientos del txt podemos correr el siguiente comando:

        pip install requirements.txt

Luego, podrá correr el programa ejecutando el siguiente comando en la terminal:

Windows 

        py Security.py

MAC

        $ sudo python3 Security.py


## Parte 2: Crear el programa de restauración
El programa de restauración debe cumplir los siguientes requisitos:

- Recibir como entrada la ruta de la carpeta de la copia de seguridad y la ruta de la carpeta donde se restaurarán los archivos.
- Leer los fragmentos de la carpeta de la copia de seguridad en el orden adecuado y restaurarlos en la carpeta original.
- Imprimir un mensaje indicando que la restauración se ha completado con éxito.


Entrega
Una vez completada la práctica, se debe entregar un archivo comprimido con los siguientes elementos:
El código fuente de los programas de copia de seguridad y restauración.
Un archivo README que explique cómo utilizar los programas y cualquier otra información relevante.
La entrega se completa con la sustentación.

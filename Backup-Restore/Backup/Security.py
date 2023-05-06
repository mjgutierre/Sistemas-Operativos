#- Recibir como entrada la ruta de la carpeta que se desea copiar y la ruta de la carpeta donde se guardarán los 
# fragmentos de la copia de seguridad.
#- Dividir los archivos de la carpeta original en varios fragmentos de tamaño máximo de 512 MB, y guardarlos en 
# la carpeta de la copia de seguridad.
#- Nombrar los fragmentos de la copia de seguridad de forma que se pueda identificar fácilmente a qué carpeta pertenecen 
#y en qué orden deben ser restaurados.
#- Imprimir un mensaje indicando que la copia de seguridad se ha completado con éxito.
#- Crear un archivo en formato JSON con la composición del archivo backup, es decir, con los archivos respaldados, 
#sus tamaño y cuantos archivos de 512 MB ser crearon.

import os
import json
import shutil

#Rutas de archivos (Fuente-Destino)
source_folder = "C:/Users/USER/Downloads/WhatsApp Unknown 2023-03-29 at 20.35.46"
destination_folder = "D:/Backup"

def backup_file(filepath, dest_folder):
    # Define el tamaño máximo de los fragmentos (en bytes)
    chunk_size = 512 * 1024 * 1024
    
    # Crea la carpeta de la copia de seguridad si no existe
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Divide el archivo original en fragmentos y los guarda en la carpeta de la copia de seguridad
    with open(filepath, 'rb') as f: 
        #abre el fichero en modo read binary, lo que permite leerlo por chunks y el loop los lee hasta llegar al final
        index = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            #Para cada chunk del archivo, genera un nombre para copiarlo en el archivo de copia de seguridad
            chunk_name = os.path.join(dest_folder, f'{os.path.basename(filepath)}.part{index}')
            with open(chunk_name, 'wb') as chunk_file:
                chunk_file.write(chunk)
            index += 1
        #el bucle incrementa la variable y la devuelve cuando todos los trozos del archivo han sido recorridos y respaldados. 
        return index


# Crea la carpeta de la copia de seguridad si no existe
def backup_folder(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Itera sobre todos los archivos de la carpeta original y los divide en fragmentos
    backup_data = [] 
    '''inicializa una lista vacía para contener los datos de copia de seguridad de cada archivo, nos servira
    para guaradar la info en json'''
    for root, dirs, files in os.walk(src_folder): #Recorre todos los archivos de la carpeta fuente
        for file in files:
            file_path = os.path.join(root, file)

            dest_subfolder = os.path.relpath(root, src_folder)
            dest_file = os.path.join(dest_folder, dest_subfolder, file)
            dest_file_folder = os.path.dirname(dest_file)
            dest_file = os.path.join(dest_folder, dest_subfolder, file)
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            num_parts = backup_file(file_path, dest_file_folder)
            #datos del json
            backup_data.append({
                'filepath': os.path.relpath(file_path, src_folder),
                'size': os.path.getsize(file_path),
                'num_parts': num_parts
            })
    
    #la lista backup_data contiene los datos de backup de todos los archivos respaldados, 
    #y se guardaran en un archivo JSON en la carpeta_dest
    with open(os.path.join(dest_folder, 'backup.json'), 'w') as f:
        json.dump(backup_data, f, indent=2)
    
    print(f"Copia de seguridad completada con éxito, los archivos estaran almacenados en {destination_folder}.")


# Ejemplo de uso:
backup_folder(source_folder,destination_folder)

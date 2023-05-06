import os
import shutil

#en este caso toma la carpeta de backup y las restaura
def restore_backup(backup_folder, restore_folder):
    # Crea la carpeta de destino si no existe
    if not os.path.exists(restore_folder):
        os.makedirs(restore_folder)
    
    # Recorre todos los archivos de la carpeta de copia de seguridad y los restaura en la carpeta de destino
    for root, dirs, files in os.walk(backup_folder):
        for file in files:
            if file.endswith('.part0'):  # Solo procesa el primer fragmento de cada archivo
                file_path = os.path.join(root, file)
                dest_subfolder = os.path.relpath(root, backup_folder)
                dest_file = os.path.join(restore_folder, dest_subfolder, file[:-5])
                dest_file_folder = os.path.dirname(dest_file)
                if not os.path.exists(dest_file_folder):
                    os.makedirs(dest_file_folder)
                
                # Copia el archivo original desde los fragmentos
                with open(dest_file, 'wb') as dest:
                    index = 0
                    while True:
                        chunk_name = os.path.join(root, f'{file[:-5]}.part{index}')
                        if not os.path.exists(chunk_name):
                            break
                        with open(chunk_name, 'rb') as chunk:
                            shutil.copyfileobj(chunk, dest)
                        index += 1
                
    print(f"Restauración completada con éxito en la carpeta {restore_folder}.")


# Ejemplo de uso
backup_folder = "D:/Backup"
restore_folder = "C:/Users/USER/Restored_Files"
restore_backup(backup_folder, restore_folder)

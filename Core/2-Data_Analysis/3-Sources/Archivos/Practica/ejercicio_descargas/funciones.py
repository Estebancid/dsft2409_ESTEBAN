import os
import shutil

def mover_archivo(source_folder, carpeta_destino, archivo):
    source = os.path.join(source_folder, archivo)
    destination = os.path.join(carpeta_destino, archivo)
    shutil.move(source, destination)
    print(f'Movido a la carpeta doc_types: {archivo}')
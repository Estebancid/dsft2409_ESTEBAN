import os
import shutil
from variables import *
from funciones import *

os.chdir('/Users/estebancid_/Downloads/Descargas_prueba')
os.getcwd()
os.listdir()

source_folder = '/Users/estebancid_/Downloads/Descargas_prueba'
for i in os.listdir():
    if i.endswith(tuple(doc_types)):
        destino = '/Users/estebancid_/Downloads/Descargas_prueba/doc_types'
        mover_archivo(source_folder, destino, i)
    elif i.endswith(tuple(img_types)):
        destino = '/Users/estebancid_/Downloads/Descargas_prueba/img_types'
        mover_archivo(source_folder, destino, i)
    elif i.endswith(tuple(software_types)):
        destino = '/Users/estebancid_/Downloads/Descargas_prueba/software_types'
        mover_archivo(source_folder, destino, i)
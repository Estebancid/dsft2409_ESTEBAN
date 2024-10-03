
import pprint

def menu_biblioteca():
    '''
    Muestra el menú de opciones de la biblioteca
    '''
    accion = input('Elige una opción:\n'
                '1. Imprimir biblioteca\n'
                '2. Buscar libro por título\n'
                '3. Añadir un libro\n'
                '4. Eliminar un libro\n'
                '5. Salir de la biblioteca')
    return accion

def mostrar_biblioteca():
    '''
    Imprime el contenido de la biblioteca
    '''
    if len(biblioteca) != 0:
            pprint.pprint(biblioteca)
    else:
        print('La biblioteca está vacía')

def buscar_titulo():
    '''
    Solicita un título y busca si está en la biblioteca o no
    '''
    title_search = input("Escribe el título del libro que quieres buscar")
    encontrado = False
    for i, libro in enumerate(biblioteca):
        if libro['título'].lower() == title_search.lower():
            print('Título encontrado')
            print(libro)
            encontrado = True
            break # el break es para que cuando encuentre el libro buscado, deje de buscar. Útil si hay muchos libros en la biblioteca para optimizar el tiempo de procesamiento.
    if encontrado == False:
        print('No se encontró ningún libro con ese título')
    return libro

def add_libro():
    '''
    Añade un nuevo libro a la biblioteca
    '''
    new_title = input('Introduce el título del libro que quieres añadir')
    new_author = input('introduce el autor del libro que quieres añadir')
    try:
        new_year = int(input('Introduce el año de publicación del nuevo libro que quieres añadir'))
    except Exception:
        print('El año debe ser un número. Se introducirá el valor por defecto 0')
        año = 0
    new_book = {'título': new_title,
        'autor': new_author,
        'año': new_year}
    biblioteca.append(new_book)
    print('Añadido a la biblioteca el libro', new_title)
    pprint.pprint(biblioteca)

def borrar_por_autor():
    '''
    Elimina un libro buscandolo por autor. Si encuentra más de un libro de ese autor, solicita el título
    '''
    autor_borrar = input('elige un autor para borrar su libro')
    libros_del_autor = 0
    for i in range(len(biblioteca)):
        if biblioteca[i]['autor'].lower() == autor_borrar.lower():
            libro_borrar = biblioteca[i]
            indice_borrar = i
            libros_del_autor = libros_del_autor + 1
    if libros_del_autor == 0:
        print('No se ha encontrado ningún libro del autor', autor_borrar)
    elif libros_del_autor == 1:
        print(f'Del autor {autor_borrar} se ha encontrado el siguiente libro:')
        print(libro_borrar)
        confirm_borrar = input(f"¿Seguro que quieres borrar el libro {libro_borrar['título']}?(Sí/No)")
        if confirm_borrar.lower() in ['sí', 'si']:
            biblioteca.pop(indice_borrar)
            print('Libro borrado')
            pprint.pprint(biblioteca)
        else:
            print('Acción cancelada. No se borrará ningún libro')
    else:
        print('Se encontraron varios libros de ese autor en la biblioteca. Busca por título')
        title_search = input("Escribe el título del libro que quieres borrar")
        encontrado = False
        for i in range(len(biblioteca)):
            if biblioteca[i]['título'].lower() == title_search.lower():
                encontrado = True
                print('Título encontrado')
                print(biblioteca[i])
                indice_borrar = i
                conf_borrar = input(f'¿Desea borrar el libro {title_search} ?(Sí/No)')
                if conf_borrar.lower() in ['sí', 'si']:
                    biblioteca.pop(indice_borrar)
                    print('Libro borrado')
                    pprint.pprint(biblioteca)
                else:
                    print('Acción cancelada. No se borrará ningún libro')

        if encontrado == False:
            print('No se ha encontrado ningún libro con ese título')
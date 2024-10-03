
from funciones_biblioteca import *


# Creamos una biblioteca con 3 libros inicialmente
libro1 = {'título': 'El Padrino',
          'autor': 'Mario Puzo',
          'año': 1969}
libro2 = {'título': 'Hábitos Atómicos',
          'autor': 'James Clear',
          'año': 2020}
libro3 = {'título': 'Extraños en un tren',
          'autor': 'Patricia Highsmith',
          'año': 1951}
biblioteca = [libro1,libro2,libro3]

# Creamos el menú y el bucle para que el menú siga activo mientras el usuario no indique salir
cerrar_biblioteca = False
while cerrar_biblioteca == False:
    print()
    accion = menu_biblioteca()

    if accion == '5':
         print('Salir de la biblioteca')
         cerrar_biblioteca = True
    
    elif accion == '1':
        mostrar_biblioteca()
    
    elif accion == '2':
        buscar_titulo()
    
    elif accion == '3':
        add_libro()
    
    elif accion == '4':
        borrar_por_autor()
    
    else:
        print('Introduce un número correcto')

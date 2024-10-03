from funciones_calculadora import *

salir = False
while not salir:
    print()
    opcion = menu_calculadora()

    if opcion == '5':
        print('Salir de la calculadora')
        salir = True

    elif opcion == '1':
        print('Operación: Suma')
        resultado = suma()
        print('Resultado:', resultado)

    elif opcion == '2':
        print('Operación: Resta')
        resultado = resta()
        print('Resultado:', resultado)
    
    elif opcion == '3':
        print('Operación: Multiplicación')
        resultado = multiplicacion()
        print('Resultado:', resultado)
    
    elif opcion == '4':
        print('Operación: División')
        resultado = division()
        print('Resultado:', resultado)

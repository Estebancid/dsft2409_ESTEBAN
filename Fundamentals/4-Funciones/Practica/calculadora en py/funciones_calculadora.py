# Se definen las funciones de la calculadora
def entrada_float():
    '''
    Solicita un número y asegura que se introduce un float
    '''
    entrada_correcta = False
    while not entrada_correcta:
        try:
            num1 = float(input('Introduce un número'))
            entrada_correcta = True
        except Exception as e:
            print('Entrada incorrecta. El valor debe ser un número')
    return num1

def menu_calculadora():
    '''
    Presenta el menú de la calculadora
    '''
    op = input('Elige la operación que quieres realizar:\n'
               '1. Sumar\n'
               '2. Restar\n'
               '3. Multiplicar\n'
               '4. Dividir\n'
               '5. Salir\n')
    return op

def suma():
    num1 = entrada_float()
    num2 = entrada_float()
    return num1 + num2

def resta():
    num1 = entrada_float()
    num2 = entrada_float()
    return num1 - num2

def multiplicacion():
    num1 = entrada_float()
    num2 = entrada_float()
    return num1 * num2

def division():
    num1 = entrada_float()
    num2 = 0
    while num2 == 0:
        num2 = entrada_float()
        if num2 == 0:
            print('No es posible dividir por 0')
    return num1 / num2
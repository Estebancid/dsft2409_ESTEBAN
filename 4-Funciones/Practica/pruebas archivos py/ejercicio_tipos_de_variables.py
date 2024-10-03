
def funcion_prueba_1():
    global biblioteca       # Sirve para indicar que se va a utilizar una variable global que se llama biblioteca
    a = 1
    b = 2
    c = 3
    print(a,b,c)
    print(biblioteca)
    print()

def funcion_prueba_2():
    funcion_prueba_3()

def funcion_prueba_3():
    print('Hola')

print()
biblioteca = [{},{},{}]

funcion_prueba_1()

funcion_prueba_2()



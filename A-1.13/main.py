"""
A-1.13 - Estructuras de control - Elif
Considera que estás desarrollando una web donde trabajas con tipos de motor (suponemos que se trata del tipo de motor de una bomba para mover fluidos). Define una variable $tipoMotor y pide al usuario que indique el número de motor mediante la función fscanf(). Los valores posibles son 1, 2, 3, 4. A través de una sentencia condicional switch debes de hacer lo siguiente:

a) Si el tipo de motor es 0, mostrar un mensaje indicando “No hay establecido un valor definido para el tipo de bomba”.

b) Si el tipo de motor es 1, mostrar un mensaje indicando “La bomba es una bomba de agua”.

c) Si el tipo de motor es 2, mostrar un mensaje indicando “La bomba es una bomba de gasolina”.

d) Si el tipo de motor es 3, mostrar un mensaje indicando “La bomba es una bomba de hormigón”.

e) Si el tipo de motor es 4,mostrar un mensaje indicando “La bomba es una bomba de pasta alimenticia”.

f) Si no se cumple ninguno de los valores anteriores mostrar el mensaje “No existe un valor válido para tipo de bomba”.
"""

def fscanf(tipoMotor):
    if tipoMotor == 0:
        print('No hay establecido un valor definido para el tipo de bomba')
    elif tipoMotor == 1:
        print('La bomba es una bomba de agua')
    elif tipoMotor == 2:
        print('La bomba es una bomba de gasolina')
    elif tipoMotor == 3:
        print('La bomba es una bomba de hormigón')
    elif tipoMotor == 4:
        print('La bomba es una bomba de pasta alimenticia')
    else:
        print('No existe un valor válido para tipo de bomba')


tipoMotor = int(input('Indica un numero de bomba: '))

fscanf(tipoMotor)

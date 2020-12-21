"""
A-1.28 - Funciones III. Divisas y multiplos
Desarrolla los siguientes supuestos que se describe a continuación.

Nota: Se valorará que no exista errores sintácticos, código limpio, funcional, que esté comentado (explicación del programa, autor, fecha de creación, alguna línea comentada que ayude a entender el código), que contenga un mínimo control de errores lógicos (Ejemplo si una función solo permite valores naturales 0,1,2,3 no permita introducir valores negativos).

"""


"""
1º Desarrolla un programa denominado Divisas, que contendrá una función denominada Conversor que debe leer un número real y un tipo de moneda (libra, dólar, yen) como valores de entrada. La función convertirá la cantidad en euros al tipo de moneda correspondiente. Por ejemplo, si la cantidad es 15 y la moneda es "dólar", se supondrá que se trata de 15 € y que hay que convertirlos a dólares y, por lo tanto, el resultado debe ser 17,37 dólares.

Deberá realizar el diagrama de flujo, el pseudocódigo y el programa en Python. (35%)
"""


def Conversor(moneda, tipo):
    if tipo == 'dolar':
        return moneda * 1.18
    elif tipo == 'libra':
        return moneda * 0.91
    elif tipo == 'yen':
        return moneda * 0.0080
    else:
        return moneda


print(Conversor(15, 'dolar'))

"""
2º Desarrolla un programa que determine la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa.

Cuando las horas exceden de 40, el resto se consideran horas extras y que éstas se pagan al doble de una hora normal cuando no exceden de 8. Sí las horas extras exceden de 8 se pagan al triple.

Deberá crear una función que tenga como valores de entrada el número de horas trabajadas y el precio por hora.

Realiza sólo el programa en Python (25%)
"""


def Salario(horas, precio):
    sueldo = 0
    for i in range(1, horas + 1):
        if i > 48:
            sueldo += precio * 3
        elif i > 40:
            sueldo += precio * 2
        elif i <= 40:
            sueldo += precio
    return sueldo


print(Salario(50, 10))


"""
3º Desarrolle un programa que nos presente un menú con 3 opciones. Eligiendo la opción “a” nos escribirá todos los múltiplos de 11 comprendidos entre 1 y 100. Eligiendo la opción “b” lo mismo, pero con los múltiplos de 17. Eligiendo la opción “c” lo mismo, pero con los múltiplos de 23. Para el desarrollo de este programa debes crear 3 funciones donde se desarrollarán cada una de las opciones. Además, se creará un procedimiento que contendrá el menú con las tres opciones y las llamadas a las funciones anteriormente descritos. Realiza sólo el programa en Python. (40%)
"""


def Multiplos11():
    n = 11
    multiplos = []
    for i in range(1, 101):
        if n * i >= 100:
            break
        multiplos.append(n * i)
    return multiplos


def Multiplos17():
    n = 17
    multiplos = []
    for i in range(1, 101):
        if n * i >= 100:
            break
        multiplos.append(n * i)
    return multiplos


def Multiplos23():
    n = 23
    multiplos = []
    for i in range(1, 101):
        if n * i >= 100:
            break
        multiplos.append(n * i)
    return multiplos


def Menu(opcion):
    if opcion == 'a':
        print(Multiplos11())
    elif opcion == 'b':
        print(Multiplos17())
    elif opcion == 'c':
        print(Multiplos23())
    else:
        print('Opcion incorrecta')


opcion = input('opciones: [a,b,c]')
Menu(opcion)

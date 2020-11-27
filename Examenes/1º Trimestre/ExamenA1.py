"""
1. (2,5 puntos) Escribir un programa que compruebe si dos número naturales leídos por teclado son primos relativos. Dos números naturales se llaman primos relativos si el máximo común divisor entre ellos es 1.
AYUDA: Los números 6 y 9 no son primos relativos ya que los divisores de 6 son 1, 2, 3 y 6, mientras que los divisores de 9 son 1, 3 y 9. Por lo tanto, el máximo común divisor de ambos números es el 3. Por otra parte, los números 9 y 14 son primos relativos, ya que los divisores de 9 son 1, 3 y 9, mientras que los divisores de 14 son 1, 2, 7 y 14. Por lo tanto, el máximo común divisor es 1.
Entrada 1: 6
Entrada 2: 9
Salida: No son primos relativos
Entrada1: 9
Entrada2: 14
Salida: Son primos relativos


2. (2,5 puntos) La NASA ha captado una comunicación extraterrestre compuesta exclusivamente de 1 y 0, por ejemplo 00111000110001101111111 y se cree que esta secuencia codifica un número cabalístico. Este número estaría descompuesto en sus factores primos y cada factor aparecería en la secuencia como la longitud de cada secuencia concreta de valores 1. Por ejemplo la secuencia anterior codificaría los números primos 3, 2, 2 y 7, lo que nos da el número cabalístico 84=3*2*2*7. Se pide, construir un programa que lea la secuencia de números como un vector y determine el número cabalístico oculto.
Entrada: 0 0 1 1 1 0 0 0 1 1 0 0 0 1 1 0 1 1 1 1 1 1 1
Salida: RESULTADO = 84

3. (2,5 puntos) Escribe un programa que contenga una función que permita codificar el nombre de una persona de acuerdo al siguiente algoritmo: leer el nombre y los dos apellidos (en tres cadenas de caracteres diferentes) y calcular e imprimir el usuario concatenando la primera letra del nombre, las tres primeras letras del primer apellido y las tres primeras letras del segundo apellido . Por ejemplo, “Juan Pérez García” se codifica como “jpergar” todo en minúscula y sin tildes.
AYUDA: Convertir la cadena a minúsculas con la función “lower(...)” y reemplazar las vocales con tildes por vocales sin tildes mediante “replace(...)”.

4. (2,5 puntos) Elabore una función recursiva que reciba como cadena de caracteres un número entero decimal y retorne su equivalente en base octal.
AYUDA: Se divide consecutivamente el número entero entre 8 (la base) y se concatenan los restos obtenidos de la división de forma sucesiva.
"""


def primera():
    n1 = int(input('Numero nº1: '))
    n2 = int(input('Numero nº2: '))
    lista1 = []
    lista2 = []
    for i in range(2, n1):
        if n1 % i == 0:
            lista1.append(i)
    for i in range(2, n2):
        if n2 % i == 0:
            lista2.append(i)
    if lista1[-1] != lista2[-1]:
        print('Son primos relativos')
    else:
        print('No son primos relativos')


#primera()


def segunda(binario):
    binario = ''.join(str(x) for x in binario)
    a = binario.split('0')
    a = list(filter(None, a))
    n = 1
    for i in a:
        n *= len(i)
    print(n)


# segunda([0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1])


def tercera(nombre, apellido1, apellido2):
    nombre = nombre.lower()
    apellido1 = apellido1.lower()
    apellido2 = apellido2.lower()

    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for r in replacements:
        nombre = nombre.replace(r[0], r[1])
        apellido1 = apellido1.replace(r[0], r[1])
        apellido2 = apellido2.replace(r[0], r[1])
    print(f'{nombre[:1]}{apellido1[:3]}{apellido2[:3]}')


# tercera("Juan", "Pérez", "García")


def cuarta(n):
    if int(n / 8) == 0:
        return str(int(n % 8))
    return str(cuarta(int(n / 8))) + str(int(n % 8))


""" for i in range(1, 20):
    print(cuarta(i)) """

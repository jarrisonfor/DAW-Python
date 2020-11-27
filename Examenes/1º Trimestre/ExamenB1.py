"""
1. (2,5 puntos) Muchos números naturales se pueden generar como suma de números consecutivos. Por ejemplo:
• 6 = 1 + 2 + 3
• 15 = 1 + 2 + 3 + 4 + 5
Escribir un programa que compruebe si un número entero leído desde el teclado cumple esta propiedad.
Entrada: 15
Salida: SI LA CUMPLE
Entrada: 20
Salida: NO LA CUMPLE


2. (2,5 puntos) El método RLE (Run Length Encoding) codifica una secuencia de datos formada por series de valores idénticos consecutivos como una secuencia de parejas de números (valor de la secuencia y número de veces que se repite). Realizar un programa que lea como un vector una secuencia de números naturales que se supone codificada con el método RLE y obtenga la secuencia decodificada. AYUDA: Las posiciones pares del vector almacenan el número de repeticiones, mientras que y las impares indican el número a repetir.
Entrada: 31526315
(tres veces 1, cinco veces 2, seis veces 3, una vez 5)
Salida: 111222223333335

3. (2,5 puntos) Dado un mensaje introducido por teclado, llevar a cabo su traducción a código Morse teniendo en cuenta que cada letra del alfabeto se sustituye por una secuencia de puntos y rayas de la siguiente manera:
a .- h .... o --- v ...- b -... i .. p .--. w .-- c -.-. j .--- q --.- x -..- d -.. k -.- r .-. y -.-- e . l .-.. s ... z --.. f ..-. m -- t - g --.  n -. u ..-
NOTA: Los espacios en blanco no requieren de traducción a código Morse.

4. (2,5 puntos) Confeccione una función recursiva que reciba un número natural y retorne un string conteniendo su equivalente hexadecimal. AYUDA: Se divide consecutivamente el número entero por 16 (la base) y se concatenan los restos de la división. Obviamente, los números 10, 11, 12, 13, 14, 15 deben ser sustituidos por A, B, C, D, E y F respectivamente durante la concatenación, es decir, no pueden ser sustituidos una vez terminada la recursividad.
"""


def primera():
    n = int(input('Dime un numero: '))
    suma = 0
    for i in range(1, n):
        suma += i
        if suma == n:
            print('SI LA CUMPLE')
            exit()
    print('NO LA CUMPLE')


# primera()


def segunda(n):
    resultado = ''
    for i in range(0, len(n), 2):
        resultado += str(n[i + 1]) * int(n[i])
    print(resultado)


# segunda('31526315')


def tercera(frase):
    morse = (
        ("a", ".-"),
        ("h", "...."),
        ("o", "---"),
        ("v", "...-"),
        ("b", "-..."),
        ("i", ".."),
        ("p", ".--."),
        ("w", ".--"),
        ("c", "-.-."),
        ("j", ".---"),
        ("q", "--.-"),
        ("x", "-..-"),
        ("d", "-.."),
        ("k", "-.-"),
        ("r", ".-."),
        ("y", "-.--"),
        ("e", "."),
        ("l", ".-.."),
        ("s", "..."),
        ("z", "--.."),
        ("f", "..-."),
        ("m", "--"),
        ("t", "-"),
        ("g", "--."),
        ("n", "-."),
        ("u", "..-"),
    )
    for r in morse:
        frase = frase.replace(r[0], r[1])
    print(frase)


#tercera('hola adios')


def cuarta(n):
    hexa = (
        ("10", "A"),
        ("11", "B"),
        ("12", "C"),
        ("13", "D"),
        ("14", "E"),
        ("15", "F"),
    )
    if n < 16:
        for r in hexa:
            n = str(n).replace(r[0], r[1])
        return n
    for r in hexa:
        l = str(int(n % 16)).replace(r[0], r[1])
        if not(l.isnumeric()):
            break
    return str(cuarta(int(n/16))) + l


# print(cuarta(15))

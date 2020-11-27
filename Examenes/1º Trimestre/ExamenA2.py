"""
1. (2,5 puntos) Una tienda ofrece un descuento del 5% o del 15% sobre el total de las compras realizadas dependiendo del tipo de cliente. Realizar un programa que solicite al usuario un tipo de cliente (identificado por 1 o 2), cantidad de productos comprados, e importe de cada uno. El funcionamiento del algoritmo es el que se detalla a continuación:
• Se le solicitará al usuario el tipo de cliente.
• Se le solicitará al usuario la cantidad de productos a calcular.
• Se le solicitará al usuario que introduzca el importe de cada uno de los productos, hasta tener el precio de todos los productos acumulado.
• Finalmente, se mostrará por pantalla la suma total de los productos que llamaremos subtotal y el total de la venta después de aplicar el descuento dependiendo del tipo de cliente.

2. (2,5 puntos) Crear un programa que reciba una frase y diga si es un pangrama o no. Sólo deberás considerar las letras del alfabeto inglés (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z), así que no te preocupes por las vocales acentuadas ni la ñ, entre otras.
AYUDA: Seguro que has visto textos como "El veloz murciélago hindú comía feliz cardillo y kiwi”, Se trata de un "pangrama", textos que contienen todas las letras de un cierto alfabeto incluso repetidas.

3. (2,5 puntos) Diseñar un programa para una caja de un supermercado que lea un precio desde el teclado y una cantidad entregada. Se debe comprobar que tanto la cantidad como el precio deben estar por debajo de los 500 euros y obviamente, cantidad debe ser mayor o igual que precio. El programa imprimirá por pantalla el número de billetes y monedas que se deben entregar de cambio, empleando para ello y por simplicidad los siguientes billetes y monedas: 100, 50, 10, 2, 1, 0.50, 0.10 y 0.01 euros.

4. (2,5 puntos) Programar una función recursiva con el siguiente pseudocódigo que permita multiplicar todos los elementos de un vector.
def multiplicar (vector, i = ultimaposicion) :
Si i == 0: # Primera posición
#Caso base cuando llegamos al primer elemento y no podemos continuar. Sino:
return (vector[i])
return (vector [i] * multiplicar (vector, i - 1));
}

"""


def primera():
    suma = []
    tipo = int(input('Introduzca tipo cliente: '))
    cantidad = int(input('Introduzca cantidad de productos: '))
    for i in range(cantidad):
        suma.append(int(input(f'Introduzca importe {i + 1}: ')))
    print(f'subtotal: {sum(suma)}€')
    if tipo == 1:
        print(f'total: {sum(suma) * 0.95}€')
    else:
        print(f'total: {sum(suma) * 0.85}€')


def segunda(frase):
    frase = frase.lower()
    abc = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    pangrama = True
    for i in abc:
        if frase.find(i) == -1:
            pangrama = False
    if pangrama:
        print('Es un pangrama')
    else:
        print('No es un pangrama')


# segunda('El bveloz murcielagjo hindu cqomía fpelizs cardillox yt kiwi')


def tercera():
    dinero = [100, 50, 10, 2, 1, 0.50, 0.10, 0.01]
    cantidad = int(input('Introduzca cantidad de productos: '))
    importe = float(input(f'Introduzca importe: '))
    total = cantidad * importe
    print('___________________________')
    print(f'Total: {"{:,.2f}".format(total)}€')
    if total >= 500 or cantidad < importe:
        print('___________________________')
        print('Cantidad o importe incorrectos')
        return
    aDevolver = 500 - total
    print(f'Total a devolver: {"{:,.2f}".format(aDevolver)}€')
    print('___________________________')
    aDevolver = round(aDevolver, 2)
    cambio = []
    j = 0
    for i in dinero:
        cambio.append(0)
        while aDevolver >= i:
            cambio[j] += 1
            aDevolver = round(aDevolver - i, 2)
        if cambio[j] > 0:
            if i <= 2:
                print(f'{cambio[j]} moneda/s de {"{:,.2f}".format(i)}€')
            else:
                print(f'{cambio[j]} billete/s de {"{:,.2f}".format(i)}€')
        j += 1


def cuarta(vector, i):
    if i == 0:
        return (vector[i])
    else:
        return (vector[i] * cuarta(vector, i - 1))

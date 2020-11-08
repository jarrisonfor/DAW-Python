"""
A-1.10 - Sentencias condicionales (II). Completar código
Añadir las condiciones en el interior de las sentencias "if" del siguiente programa, para que los mensajes se muestren de forma correcta:

numero1 = 5

numero2 = 8

if(...) :

    print("numero1 no es mayor que numero2")

if(...):

    print("numero2 es positivo")

if(...):

    print("numero1 es negativo o distinto de cero")

if(...):

    print("Incrementar en 1 unidad el valor de numero1 no lo hace mayor o igual que numero2")
"""


numero1 = 5

numero2 = 8

if(numero1 < numero2):
    print("numero1 no es mayor que numero2")

if(numero2 >= 0):
    print("numero2 es positivo")

if(numero1 < 0 or numero1 != 0):
    print("numero1 es negativo o distinto de cero")

if(numero1 + 1 < numero2):
    print("Incrementar en 1 unidad el valor de numero1 no lo hace mayor o igual que numero2")

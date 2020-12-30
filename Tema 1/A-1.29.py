"""
A-1.29 - Matrices (IV) - Comprobador de cuadrado mágico
Un cuadrado mágico es una disposición de números naturales en una matriz cuadrada, de modo que las sumas de cada columna, de cada fila y de cada diagonal son iguales.

Escriba una función que reciba una matriz e indique si se trata o no de un cuadrado mágico:

correcto = es_magico(array((3, 1, 5),
...                        (4, 7, 2),
...                        (9, 8, 6)))

Falso. No es un cuadrado mágico

correcto = es_magico(array((2, 7, 6),
...                        (9, 5, 1),
...                        (4, 3, 8)))

Correcto. Es un cuadrado mágico.
"""

arrayMagica = ((2, 7, 6), (9, 5, 1), (4, 3, 8))

arrayNoMagico = ((3, 1, 5), (4, 7, 2), (9, 8, 6))


def es_magico(a):
    check = sum(a[0])
    diagonal1 = []
    diagonal2 = []
    for i in range(len(a)):
        if sum(a[i]) != check:
            return False
        if sum([a[j][i] for j in range(len(a))]) != check:
            return False
        diagonal1.append(a[i][i])
        diagonal2.append(a[i][len(a)-i-1])
    if sum(diagonal1) != check:
        return False
    if sum(diagonal2) != check:
        return False
    return True


correcto = es_magico(arrayMagica)

if correcto:
    print('Correcto. Es un cuadrado mágico')
else:
    print('Falso. No es un cuadrado mágico')

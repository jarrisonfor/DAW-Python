"""
A-1.35 - Recursividad. Invertir una lista
Escriba una función recursiva que invierta una lista de enteros basándose en la siguiente idea:

Cree una función que se le pase como parámetros la propia lista y la posición del elemento inicial y final de la misma.
Los valores que ocupan las posiciones iniciales y finales serán intercambiados.
Se llamará recursivamente incrementando la posición del elemento inicial en uno y decrementando la posición del elemento final en uno.
"""


def invertir(array, j=0, i=0):
    if i == 0:
        j = len(array) - 1
    if i < j:
        array[i], array[j] = array[j], array[i]
        return invertir(array, j - 1, i + 1)
    else:
        return array


print(invertir([1, 2, 3, 4, 5, 6, 7, 8]))

"""
A-1.35 - Recursividad. Algoritmo rápido de ordenación Quicksort
Dada la siguiente implementación del algoritmo QuickSort, añadir al código fuente algunas posibles modificaciones (p.e. cambiar la forma de escoger el pivote) que permitan mejorar la  eficiencia del algoritmo.

QuickSort (en inglés, ordenamiento rápido). Es un algoritmo basado en la técnica de divide y vencerás, que permite, en promedio, ordenar n elementos en un tiempo proporcional a n log n.

El algoritmo consta de los siguientes pasos:

Elegir un elemento de la lista de elementos a ordenar, al que llamaremos pivote.
Resituar los demás elementos de la lista a cada lado del pivote, de manera que a un lado queden todos los menores que él, y al otro los mayores. Los elementos iguales al pivote pueden ser colocados tanto a su derecha como a su izquierda, dependiendo de la implementación deseada. En este momento, el pivote ocupa exactamente el lugar que le corresponderá en la lista ordenada. La lista queda separada en dos sublistas, una formada por los elementos a la izquierda del pivote, y otra por los elementos a su derecha.
Repetir este proceso de forma recursiva para cada sublista mientras éstas contengan más de un elemento.
Una vez terminado este proceso todos los elementos estarán ordenados.
"""

import math


def partition(arr, low, high):
    i = (low-1)
    """
    Elegimos de pivot, el item de la mitad de la array
    De esta manera si un array esta semi ordenada o ordenada, no ira todo a un solo lado, se dividira si o si
    """
    pivot = arr[math.floor(len(arr) - 1 / 2)]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])

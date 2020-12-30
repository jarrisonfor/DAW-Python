"""
A-1.34 - Recursividad. Ordenar de menor a mayor
Escriba una función recursiva que ordene de menor a mayor un arreglo de enteros basándose en la siguiente idea: coloque el elemento más pequeño en la primera ubicación, y luego ordene el resto del arreglo con una llamada recursiva.
"""

import random
randomlist = [0]
for i in range(0, 5):
    n = random.randint(1, 100)
    randomlist.append(n)


def ordenar(array, i=0):
    if i == len(array) - 1:
        return array
    if array[i] > array[i+1]:
        array[i], array[i+1] = array[i+1], array[i]
    else:
        i += 1
        return ordenar(array, i)
    return ordenar(array, 0)


print(randomlist)
print(ordenar(randomlist))

"""
A-1.21 - Listas de elementos generados aleatoriamente
1. Se tiene una lista de 125 elementos con valores numéricos enteros generados de forma aleatoria. Se debe realizar lo siguiente:

Leer un valor x y buscar en qué posición de la lista se encuentra
Llenar otra lista con los elementos de las posiciones impares del vector dado.
En esta última lista, busque cuántos elementos son múltiplos de 3 y positivos.
2.
"""

import random
randomlist = []
for i in range(0, 125):
    n = random.randint(-125, 125)
    randomlist.append(n)

numero = int(input('Dime un numero: '))
try:
    print(f'La posicion de tu numero es: {randomlist.index(numero)}')
except:
    print('El valor introducido no existe en la lista')

lista = []
contador = 0
for i in range(0, 126, 2):
    lista.append(randomlist[i])
    if randomlist[i] % 3 == 0 and randomlist[i] > 0:
        contador += 1

print(f'Hay {contador} numeros que son multiplos de 3 y son positivos\n')
print(lista)

"""
A-1.22 - Estructuras de control - Bucles Anidados. Método de la Burbuja
Escriba un programa que implemente el "Método de la Burbuja".

La Ordenación de burbuja (Bubble Sort ) es un sencillo algoritmo de ordenación. Funciona revisando cada elemento de la lista que va a ser ordenada con el siguiente, intercambiándolos de posición si están en el orden equivocado. Es necesario revisar varias veces toda la lista hasta que no se necesiten más intercambios, lo cual significa que la lista está ordenada.
"""

array = [54326, 2, 3, 5, 65, 5324, 34, 324, 5, 23,
         61, 6, 123, 52334, 2, 562, 34, 5, 12, 4223]
for i in range(1, len(array)):
    for j in range(0, len(array)-i):
        if(array[j] > array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]
print(array)

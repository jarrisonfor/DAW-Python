"""
A-1.16 - Estructuras de control - Obtener el mayor y el menor de N números introducidos
Desarrollar una aplicación que pregunte inicialmente cuantos números se van a introducir por teclado, los solicite y devuelva por pantalla el número mayor y el menor. AYUDA: Utilizar una variable “mayor” y otra "menor" que almacene en cada instante el número más grande y el más pequeño encontrado respectivamente. En cada iteración, se comprobará si el número introducido es más grande que el que tenemos almacenado en “mayor” y en caso afrmativo, se actualizará su valor. Para el menor, en cada iteración se comprobará si el número introducido es más pequeño que el que tenemos almacenado en “menor” y en caso afrmativo, se actualizará su valor.

EJECUCIÓN:
--------------------------------
¿Cuántos números va a introducir? 4
Introduzca número 1: 4
Introduzca número 2: 7
Introduzca número 3: 6
Introduzca número 4: 1
---------------------------------
El mayor es el 7

El menor es el 1
"""

numero = int(input('Dígame cuántos números va a escribir: '))
mayor = -999999999999
menor = 9999999999999

for i in range(1, numero + 1):
    n = int(input(f'Dígame el número {i}: '))
    if n < menor:
        menor = n
    if n > mayor:
        mayor = n

print(f'El mayor es el {mayor}')
print(f'El menor es el {menor}')

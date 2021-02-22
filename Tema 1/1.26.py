"""
A-1.26 - Funciones I - Números primos
Definir una función que determine si un número entero pasado como argumento es primo, es decir, si únicamente es divisible por si mismo y por uno. Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.

EJEMPLO:

El número 5 es primo, ya que para todos aquellos números comprendidos entre 1 y 5 (1,2,3,4,5) , únicamente se obtiene resto cero al dividir el número entre 1 o entre el propio 5.
El número 4 no es primo, ya que para todos aquellos números comprendidos entre 1 y 4 (1,2,3,4), se obtiene resto cero al dividir el número entre 1, 2 y 4. De esta forma, el número 4 no cumple que únicamente es divisible por sigo mismo y por uno, puesto que es múltiplo de 2.
"""

def primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(primo(7))
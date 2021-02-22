"""
A-1.15 - Estructuras de control - Bucles y Contadores
Escriba un programa que pregunte cuántos números va a introducir, pida esos números y escriba la cantidad de números pares e impares que ha escrito.

Ejemplo:

Dígame cuántos números va a escribir: 5
Dígame el número 1: 17
Dígame el número 2: 5
Dígame el número 3: 7
Dígame el número 4: 22
Dígame el número 5: 19

Ha escrito 1 número(s) par(es)
Ha escrito 4 número(s) impar(es)
"""

numero = int(input('Dígame cuántos números va a escribir: '))
pares = 0
impares = 0

for i in range(1, numero + 1):
    if int(input(f'Dígame el número {i}: ')) % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Ha escrito {pares} número(s) par(es)')
print(f'Ha escrito {impares} número(s) impar(es)')

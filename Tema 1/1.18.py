"""
A-1.18 - Estructuras de control - Bucles Anidados
Escriba un programa que muestra la tabla de multiplicar de todos los números del 1 al 10.
"""

for i in range(1, 11):
    print(f'\nTabla del {i}')
    for j in range(11):
        print(f'{i} x {j} = {i*j}')

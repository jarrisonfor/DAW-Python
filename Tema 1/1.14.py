"""
A-1.14 - Estructuras de control - Bucles y Acumuladores
El factorial de un número entero n es una operación matemática que consiste en multiplicar todos los factores n x (n-1) x (n-2) x ... x 1. Así, el factorial de 5 (escrito como 5!) es igual a: 5! = 5 x 4 x 3 x 2 x 1 = 120

Elabora dos programas (utilizando en uno de ellos la estructura for y en otro la estructura while) que permitan calcular el factorial de un número entero indicado por el usuario.
"""

numero = int(input('Dime un numero: '))
temp = 1

for i in range(1, numero + 1):
    temp = temp * i
print(temp)

temp = 1
contador = 1
while contador <= numero:
    temp = temp * contador
    contador += 1
print(temp)

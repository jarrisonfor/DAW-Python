"""
A-1.7 - Sentencias condicionales (I). Par e Impar
Escriba un programa que pregunte por un número e indique si es par o impar.

Dígame el número: 17

El número 17 es impar
"""

numero = int(input('Dime un numero: '))
print(f'El número numero es: {("par" if numero%2==0 else "impar")}')

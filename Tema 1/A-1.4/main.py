"""
A-1.4 - Operaciones aritméticas (III). Conversor de divisas
Escribir un programa que solicite por teclado un importe en euros y devuelva su conversión en las siguientes divisas:

Dólares (EEUU)
Libras (GB)
Liras turcas. (TK)
"""

euros = float(input('Dime tu sueldo: '))
print(f'Dolares: {euros * 1.18}')
print(f'Libras: {euros * 0.91}')
print(f'Liras turcas: {euros * 0.11}')

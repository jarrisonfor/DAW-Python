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

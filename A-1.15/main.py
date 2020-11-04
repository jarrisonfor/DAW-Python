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

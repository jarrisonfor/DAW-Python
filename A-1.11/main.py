numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))
numero3 = int(input('Numero 3: '))
ordenado = []

if numero1 <= numero2 and numero1 <= numero3:
    ordenado.append(numero1)
elif numero2 <= numero1 and numero2 <= numero3:
    ordenado.append(numero2)
elif numero3 <= numero2 and numero3 <= numero1:
    ordenado.append(numero3)

if numero1 >= numero2 and numero1 <= numero3 or numero1 >= numero3 and numero1 <= numero2:
    ordenado.append(numero1)
elif numero2 >= numero1 and numero2 <= numero3 or numero2 >= numero3 and numero2 <= numero1:
    ordenado.append(numero2)
elif numero3 >= numero2 and numero3 <= numero1 or numero3 >= numero1 and numero3 <= numero2:
    ordenado.append(numero3)


if numero1 >= numero2 and numero1 >= numero3:
    ordenado.append(numero1)
elif numero2 >= numero1 and numero2 >= numero3:
    ordenado.append(numero2)
elif numero3 >= numero2 and numero3 >= numero1:
    ordenado.append(numero3)

print(f'El resultado es {ordenado[0]}, {ordenado[1]} y {ordenado[2]}')

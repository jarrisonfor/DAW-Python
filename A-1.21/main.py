import random
randomlist = []
for i in range(0, 125):
    n = random.randint(-125, 125)
    randomlist.append(n)

numero = int(input('Dime un numero: '))
try:
    print(f'La posicion de tu numero es: {randomlist.index(numero)}')
except:
    print('El valor introducido no existe en la lista')

lista = []
contador = 0
for i in range(0, 126, 2):
    lista.append(randomlist[i])
    if randomlist[i] % 3 == 0 and randomlist[i] > 0:
        contador += 1

print(f'Hay {contador} numeros que son multiplos de 3 y son positivos\n')
print(lista)

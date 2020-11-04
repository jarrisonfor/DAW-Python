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

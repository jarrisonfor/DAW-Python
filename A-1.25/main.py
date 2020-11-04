import re

sospechosos = [
    ['Pedro', 'Gonzalez', '00000101010101010101'],
    ['Juan', 'Gonzalez',  '00101010101101110111'],
    ['Diego', 'Gonzalez', '00100010010000001001'],
]

secuencia = input('Ingrese secuencia: ')

if re.match("^[01]{20,20}$", secuencia):
    sospechoso = ''
    porcentaje = 0

    for s in sospechosos:
        aciertos = 0
        for i in range(len(s[2])):
            if s[2][i] == secuencia[i]:
                aciertos += 1
        temp = aciertos*100/20
        if porcentaje < temp:
            porcentaje = temp
            sospechoso = s[0]

    print(f"El culpable es {sospechoso} con un parentezco de {porcentaje}%")
else:
    print('La secuencia pasada no es un dna valido')

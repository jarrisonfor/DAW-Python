"""
A-1.20 - Cadenas de caracteres (II). El lenguaje Hacker
EL LENGUAJE HACKER
El "L3N6U4J3 H4CK3R" (o "lenguaje hacker") se originó por la necesidad de los internautas de escribir palabras que estaban censuradas en los motores de búsqueda. Para emplear este lenguaje debemos reemplazar la mayor cantidad de letras por números basándonos en su parecido físico, tal y como se detalla a continuación:

La 'O' es un 0 (cero).
La 'A' es un 4 (cuatro).
La 'E' es un 3 (tres).
La 'I' es un 1 (uno).
La 'S' es un 5 (cinco).
La 'T' es un 7 (siete).
La 'G' es un 6 (seis).
La 'B' es un 8 (ocho).
Dado un mensaje de texto, este debe ser transformado a mayúsculas y cifrado empleando para ello el Lenguaje del Hacker.

"""

frase = input('Dime una frease: ')
frase = frase.upper()
frase = frase.replace('O', '0')
frase = frase.replace('A', '4')
frase = frase.replace('E', '3')
frase = frase.replace('I', '1')
frase = frase.replace('S', '5')
frase = frase.replace('T', '7')
frase = frase.replace('G', '6')
frase = frase.replace('B', '8')

print(frase)

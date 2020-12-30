"""
A-1.19 - Cadenas de caracteres (I). Contador de caracteres
Dada una cadena texto solicitada al usuario por teclado, se debe mostrar por pantalla un mensaje con el total de caracteres y la cantidad de vocales.

AYUDA: Utilizar una función existente para el manejo de cadenas, que permita encontrar el total de caracteres dentro de un string. Además, podemos emplear una variable contadora para almacenar las apariciones de cada una de las cinco vocales. Tenga en cuenta que el número de consonantes es igual a la diferencia entre el total de caracteres y el número de vocales.

EJECUCIÓN:

---------------------------------

La cadena tiene 37 caracteres, de los cuales 13 son vocales.
"""

import re
frase = input('Dime una frease: ')
contador = 0

for letra in frase:
    if re.search("[aeiou]", letra, re.IGNORECASE):
        contador += 1

print(
    f"La cadena tiene {len(frase)} caracteres, de los cuales {contador} son vocales y {len(frase) - contador} consonantes.")

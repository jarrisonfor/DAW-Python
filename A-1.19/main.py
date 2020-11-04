import re
frase = input('Dime una frease: ')
contador = 0

for letra in frase:
    if re.search("[aeiou]", letra, re.IGNORECASE):
        contador += 1

print(
    f"La cadena tiene {len(frase)} caracteres, de los cuales {contador} son vocales y {len(frase) - contador} consonantes.")

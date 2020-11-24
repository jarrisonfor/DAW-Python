"""
A-1.36 - Recursividad. Palíndromo
Implementar el ejercicio 1.27 empleando recursividad.
"""


def palindromo(frase, j=0, i=0):
    if i == 0:
        frase = frase.strip().lower().replace(" ", "")
        j = len(frase) - 1
    if j <= i:
        return True
    elif i < j and frase[i] == frase[j]:
        return palindromo(frase, j - 1, i + 1)
    else:
        return False


print(palindromo('La ruta nos aporto otro paso natural'))

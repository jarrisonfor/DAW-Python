"""
A-1.27 - Funciones II - Palíndromo
Definir una función que determine si la cadena de texto que se le pasa como parámetro es un palíndromo, es decir, si se lee de la misma forma desde la izquierda y desde la derecha. Ejemplo de palíndromo complejo: "La ruta nos aporto otro paso natural".

AYUDA:

1. Convertir la cadena "La ruta nos aportó otro paso natural" en "larutanosaportóotropasonatural"
2. Convertir en un vector de caracteres (["l","a","r","u","t","a","n","o","s", ...]
3. Generar una copia invertida del vector aplicando la función "reverse()".
4. Comparar caracter a caracter ambos vectores empleado para ello un bucle que los recorra desde la primera posición hasta la última de ambos.
5. La función devolverá falso desde el momento que dos caracteres en una misma posición no coincidan (ya no será un palíndromo).
"""

def palindromo(f):
    f = f.strip().replace(" ", "").lower()
    if f != f[::-1]:
        return False
    return True

print(palindromo('La ruta nos aporto otro paso natural'))
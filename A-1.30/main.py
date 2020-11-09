"""
El sudoku es un puzzle que consiste en llenar una rejilla de 9 × 9 con los dígitos del 1 al 9, de modo que no haya ningún valor repetido en cada fila, en cada columna y en cada uno de las regiones de 3 × 3 marcadas por las líneas más gruesas.

El sudoku sin resolver tiene algunos de los dígitos puestos de antemano en la grilla. Cuando el puzzle ha sido resuelto, todas las casillas tienen un dígito, y entre todos satisfacen las condiciones señaladas.

En un programa, un sudoku resuelto puede ser guardado en un arreglo de 9 × 9:

from numpy import array
sr = array([[4, 2, 6, 5, 7, 1, 3, 9, 8],
            [8, 5, 7, 2, 9, 3, 1, 4, 6],
            [1, 3, 9, 4, 6, 8, 2, 7, 5],
            [9, 7, 1, 3, 8, 5, 6, 2, 4],
            [5, 4, 3, 7, 2, 6, 8, 1, 9],
            [6, 8, 2, 1, 4, 9, 7, 5, 3],
            [7, 9, 4, 6, 3, 2, 5, 8, 1],
            [2, 6, 5, 8, 1, 4, 9, 3, 7],
            [3, 1, 8, 9, 5, 7, 4, 6, 2]])
Escriba la función solucion_es_correcta(sudoku) que reciba como parámetro un arreglo de 9 × 9 representando un sudoku resuelto, y que indique si la solución es correcta (es decir, si no hay elementos repetidos en filas, columnas y regiones):

correcto = solucion_es_correcta($matriz)

La solución es correcta

"""

sudoku = [[4, 2, 6, 5, 7, 1, 3, 9, 8],
          [8, 5, 7, 2, 9, 3, 1, 4, 6],
          [1, 3, 9, 4, 6, 8, 2, 7, 5],
          [9, 7, 1, 3, 8, 5, 6, 2, 4],
          [5, 4, 3, 7, 2, 6, 8, 1, 9],
          [6, 8, 2, 1, 4, 9, 7, 5, 3],
          [7, 9, 4, 6, 3, 2, 5, 8, 1],
          [2, 6, 5, 8, 1, 4, 9, 3, 7],
          [3, 1, 8, 9, 5, 7, 4, 6, 2]]


def solucion_es_correcta(m):
    s = 0
    b = 0
    for i in range(len(m)):
        # Horizontal
        if len(m[i]) != len(set(m[i])):
            return False
        # Vertical
        vertical = [m[j][i] for j in range(len(m))]
        if len(vertical) != len(set(vertical)):
            return False
        # Bloques
        bloque = []
        for o in m[s:s+3]:
            for j in o[b:b+3]:
                bloque.append(j)
        if len(bloque) != len(set(bloque)):
            return False
        if b == 6:
            s += 3
            b = 0
        else:
            b += 3
    return True


correcto = solucion_es_correcta(sudoku)

if correcto:
    print('La solución es correcta')
else:
    print('La solución es incorrecta')

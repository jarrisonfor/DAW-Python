"""
A-1.23 - Estructuras de control - Suma de dos matrices
Implementa un programa que permita sumar dos matrices introducidas por teclado. NOTA: No todas las matrices se pueden sumar o restar entre sí. La condición necesaria para sumar o restar dos matrices es que tengan la misma dimensión, es decir, que tengan el mismo número de filas y de columnas. Para sumar matrices de la misma dimensión se suman entre sí los elementos que ocupan el mismo lugar en cada matriz.
"""

def creaMatrices():
    try:
        m = []
        nf = int(input("Introduce de cuantas filas sera tu matriz?: "))
        nc = int(input("Introduce de cuantas columnas sera tu matriz?: "))
        for i in range(nf):
            m.append([])
            for j in range(nc):
                m[i].append(int(input(f"Fila {i + 1}, Columna {j + 1}: ")))
        return m
    except:
        print('Solo se permite introducir numeros')
        return creaMatrices()


m1 = creaMatrices()
m2 = creaMatrices()

try:
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m2[i][j] = m2[i][j] + m1[i][j]
    print(m2)
except:
    print('Las matrices no contienen el mismo numero de elementos o no es una matriz')

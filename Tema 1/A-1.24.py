"""
A-1.24 - Matriz de Pascal
Una matriz de Pascal simétrica está definida como una matriz cuadrada [NxN] de la siguiente forma:

P(i,1) = P(1,j) = 1 para todo i,j
P(i,j) = P(i-1,j) + P(i,j-1) para i,j > 1           
Escribe el código de un programa que calcule una matriz de Pascal de orden n. El usuario introduce un valor para n, por teclado, y el programa calculará la matriz mostrándola por pantalla. Aquí debajo tienes un ejemplo de matriz de Pascal con N=5.
1  1  1  1  1
1  2  3  4  5
1  3  6 10 15
1  4 10 20 35
1  5 15 35 70

"""

n = int(input("Introduce tu numero de matriz de Pascal: "))
matriz = [[1 for i in range(n)] for j in range(n)]
for i in range(1, n):
    for j in range(1, n):
        matriz[i][j] = matriz[i-1][j] + matriz[i][j-1]
print(matriz)

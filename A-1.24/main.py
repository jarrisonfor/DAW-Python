n = int(input("Introduce tu numero de matriz de Pascal: "))
matriz = [[1 for i in range(n)] for j in range(n)]
for i in range(1, n):
    for j in range(1, n):
        matriz[i][j] = matriz[i-1][j] + matriz[i][j-1]
print(matriz)

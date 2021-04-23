"""
Desarrolle un programa que utilice un menú de opciones con las operaciones siguientes:

Insertar Matriz A
Insertar Matriz B
Sumar Matrices A+B
Restar Matrices A-B
Multiplicar Matrices A*B (comprobar si es posible o no)
Obtener la traspuesta de la matriz A
Obtener la traspuesta de la matriz B
Obtener el valor máximo y mínimo de la matriz A
Obtener el valor máximo y mínimo de la matriz B
Imprimir Matriz A
Imprimir Matriz B
Salir


"""




def dibujaMatriz(M):
    for i in range(len(M)):
        print('[')
        for j in range(len(M[i])):
            print('{:>3s}'.format(str(M[i][j])))
        print (']')

def matriz2str(matriz):
    cadena = ''
    for i in range(len(matriz)):
        cadena += '['
        for j in range(len(matriz[i])):
            cadena += '{:>4s}'.format(str(matriz[i][j]))
            cadena += ']\n'
    return cadena

def creaMatriz(n,m):
    '''
    Esta función crea una matríz vacía con n filas y n columnas.
    @param n : Número de filas.
    @param m : Número de columnas
    @type n: int
    @type m: int
    @return: devuelve una matriz n por m
    @rtype: matriz (lista de listas)
    '''
    matriz = []
    for i in range(n):
        a = [0]*m
        matriz.append(a)
    return matriz

def creaMatrizDato(n,m, dato):
    '''
    Esta función crea una matríz con n filas y n columnas.
    Cada celda contiene el valor "dato"
    @param n : Número de filas.
    @param m : Número de columnas
    @param dato: Un valor
    @type n: entero
    @type m: entero
    @type dato: tipo simple
    @return: devuelve una matriz n por m
    @rtype: matriz (lista de listas)
    '''
    matriz = []
    for i in range(n):
        a = [dato]*m
        matriz.append(a)
    return matriz

def matrizCorrecta(M):
    '''
    Nos dice si una matriz es correcta.
    @param M: una matriz
    @type M: matriz
    @return: True si es correcta, False en caso contrario
    '''
    filas = len(M)
    columnas = len(M[0])
    correcto = True
    i = 1
    while i < filas and correcto:
        correcto = (len(M[i]) == columnas)
        i += 1
    return correcto


def filas(M):
    '''
    Nos dice el número de filas de una matriz correcta.
    @param M: una matriz
    @type M: matriz
    @return: número de filas
    '''
    if matrizCorrecta(M):
        return len(M)

def columnas(M):
    '''
    Nos dice el número de columnas de una matriz correcta.
    @param M: una matriz
    @type M: matriz
    @return: número de columnas
    '''
    if matrizCorrecta(M):
        return len(M[0])

def matrizIdentidad(n):
    '''
    Crea una matriz identidad de tamaÃ±o n
    @param n : número de filas.
    @type n : entero
    @return: matriz identidad de tamaÃ±o n
    '''
    m = creaMatriz(n,n)
    for i in range(n):
        m[i][i] = 1
    return m

def copy(m):
    '''
    Realiza una copia independiente de la matriz
    '''
    result=[]
    for f in m:
        result.append(f[:])
    return result

def leeMatriz(n,m):
    '''
    Esta función lee por teclado una matríz con n filas y n columnas.
    @param n : Número de filas.
    @param m : Número de columnas
    @type n: entero
    @type m: entero
    @return: devuelve una matriz n por m
    '''
    A = creaMatriz(n,m)
    for i in range(n):
        for j in range(m):
            A[i][j] = int(input('Introduce la componente (%d,%d): '%(i,j)))
    return A

def sumaMatriz(A,B):
    '''
    Suma dos matrices. Las dos matrices deben ser de la misma dimensiÃ³n
    @param A: una matriz nxm
    @param B: una matriz nxm
    @type A: Matriz
    @type B: Matriz
    @return: Matriz suma
    '''
    if filas(A) == filas(B) and columnas(A) == columnas(B):
        C = creaMatriz(filas(A), columnas(A))
        for i in range(filas(A)):
            for j in range(columnas(A)):
                C[i][j] = A[i][j] + B[i][j]
        return C

def multiplicaMatriz(A,B):
    '''
    Multiplica dos matrices. El número de columnas de la primera de
    be ser igual al número de filas de la segunda.
    @param A: una matriz nxm
    @param B: una matriz mxk
    @type A: Matriz
    @type B: Matriz
    @return: Matriz multiplicación nxk
    '''
    if columnas(A) == filas(B):
        C = creaMatriz(filas(A), columnas(B))
        for i in range(filas(C)):
            for j in range(columnas(C)):
                for k in range(columnas(A)):
                    C[i][j] += A[i][k] * B[k][j]
        return C


def traspuesta(M):
    '''
    Calcula la matriz traspuesta de M
    '''
    m = len(M) #filas
    n = len(M[0]) # columnas
    T = creaMatriz(n,m)
    for i in range(n):
        for j in range(m):
            T[i][j] = M[j][i]
    return T

def multiplicaFila(m,f,e):
    '''
    Multiplica la fila f por el valor e
    '''
    n=len(m)
    for c in range(n):
        m[f][c]=m[f][c]*e

def combinacion(m,i,j,e):
    '''
    Combina las filas i y j, añadiendo a la fila j el producto de la
    fila i por un factor e
    '''
    n=len(m)
    for c in range(n):
        m[j][c]=m[j][c]+e*m[i][c]

def intercambiaFilas(m,i,j):
    m[i],m[j] = m[j],m[i]

def determinante(matriz):
    '''
    Calcula el determinante poniendo ceros debajo
    de la diagonal principal
    '''
    m = copy(matriz)
    n=len(m)
    det=1
    for i in range(n):
        j=primeroNoNulo(m,i)
        if j == n:
            return 0
        if i!=j:
            det=-1*det
            intercambiaFilas(m,i,j)
        det=det*m[i][i]
        multiplicaFila(m,i,1./m[i][i])
        for k in range(i+1,n):
            combinacion(m,i,k,-m[k][i])
    return det

def primeroNoNulo(m,i):
    '''
    A partir de la fila i, busca la primera fila j cuya entrada
    (i,j) es nula
    '''
    result=i
    while result<len(m) and m[result][i]==0:
        result=result+1
    return result

def menor(A,f,c):
    '''
    Calcula el "menor" que se obtiene a partir de A al quitar la fila f y la
    columna c.
    Suponemos que A es cuadrada
    '''
    if filas(A) == columnas(A):

        m = filas(A)
        M = creaMatriz(m-1, m-1)
        '''
        Dividimos la matriz en cuatro trozos
        [1 | 2]
        [3 | 4]
        '''
        # 1
        for i in range(f):
            for j in range(c):
                M[i][j] = A[i][j]
        # 2
        for i in range(f):
            for j in range(c,m-1):
                M[i][j] = A[i][j+1]
        # 3
        for i in range(f,m-1):
            for j in range(c):
                M[i][j] = A[i+1][j]
        # 4
        for i in range(f,m-1):
            for j in range(c,m-1):
                M[i][j] = A[i+1][j+1]
        return M

def determinante_rec(matriz):
    '''
    Calcula el determinante de forma recursiva, calculando los
    sucesivos menores
    '''
    if len(matriz) == 1:
        result = matriz[0][0]
    elif len(matriz) == 2:
        result = matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
    else:
        result = 0
        i = 0
        sig = +1
        while i < len(matriz):
            mm = menor(matriz, i, 0)
            result += sig * matriz[i][0]* determinante_rec(mm)
            sig = - sig
            i += 1
    return result
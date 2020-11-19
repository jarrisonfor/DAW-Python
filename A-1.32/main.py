"""
A-1.32 - Recursividad. Descomposiciones de un número natural
Diseñe e implemente un algoritmo que imprima todas las posibles descomposiciones de un número natural como suma de números menores que él.
1 = 1
2 = 1 + 1
3 = 2 + 1
3 = 1 + 1 + 1
4 = 3 + 1
4 = 2 + 1 + 1
4 = 1 + 1 + 1 + 1
4 = 2 + 2
5 = 3 + 2
5 = 4 + 1
5 = 2 + 2 + 1
5 = 3 + 1 + 1
5 = 2 + 1 + 1 + 1
5 = 1 + 1 + 1 + 1 + 1
N = (n-1) +1
N = (n-2) + 2 = (n-2) + 1 + 1
"""

""" https://www.geeksforgeeks.org/find-all-combinations-that-adds-upto-given-nber-2/ """


def descomponer(n, i=0, array=[],
                reducedNum=0):
    if len(array) == 0:
        array = [0] * n
        reducedNum = n
    if (reducedNum < 0):
        return
    if (reducedNum == 0):
        print(f'{n} = ' + str("%s + " *
                              len(array[0:i]) % tuple(array[0:i]))[0:-3])
        if n == 1:
            return
        if n == array[0]:
            descomponer(n - 1)
        return
    prev = 1 if(i == 0) else array[i - 1]
    for j in range(prev, n + 1):
        array[i] = j
        descomponer(n, i + 1, array, reducedNum - j)


n = int(input('Dime un numero: '))
descomponer(n)

""" for i in range(1, n + 1):
    descomponer(i) """

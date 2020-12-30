"""
A-1.31 - Recursividad. Función de Fibonacci
"""


def fibonacci(n):
    if isinstance(n, list):
        if n[0] <= n[-1]:
            n.pop(0)
            n.pop(-1)
            return n
        n.append(n[-1] + n[-2])
        return fibonacci(n)
    else:
        return fibonacci([n, 0, 1])


print(fibonacci(100))

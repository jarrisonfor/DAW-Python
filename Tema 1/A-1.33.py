"""
A-1.33 - Recursividad. Conversor a binario
Programe un método recursivo que transforme un número entero positivo a notación binaria.
"""


def conversor(n):
    if int(n / 2) == 1 or int(n / 2) == 0:
        return str(int(n / 2)) + str(int(n % 2))
    return str(conversor(int(n / 2))) + str(int(n % 2))


print(conversor(8))

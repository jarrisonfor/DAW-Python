"""
UT2-A4 Racional
Escriba una clase Racional que permita trabajar con números racionales. Esta clase es útil ya que nos permite representar números como 1/3 sin pérdida de precisión (si lo representáramos como un real (0,333333) estaríamos perdiendo precisión). Para ello, almacenaremos en la clase el numerador y el denominador del número racional.Las operaciones que nuestra clase necesitará definir son:

Construcción del objeto con parámetros.
Método para el acceso a los atributos.
Operador de asignación(=)
Operaciones aritméticas: suma, resta, producto y división.
Operadores relacionales: igualdad y todas las desigualdades (>, <, >=, <=, !=, ==).
Cambio de signo.
    positivo + positivo = positivo, etc...

Además, todos los números deben ser simplificados después de cada operación. Para ello, podemos calcular el máximo común divisor (mcd) de numerador y denominador utilizando el algoritmo de Euclides, y luego dividir ambos números por este valor:

def mcd (numerador, denominador) :

mcd, temp, resto = 0, 0, 0

mcd = Math.abs(numerador)

temp = denominador

while (temp > 0):

        resto = mcd % temp

        mcd = temp

        temp = resto

        return mcd
"""
from controllers.Racional import Racional

numero1 = Racional(5,-4)
numero2 = Racional(3,5)

numero1.setNumerador(-5)
numero1.setDenominador(-4)
numero1.cambioSigno()
print(numero1.getDenominador())
print(numero1.getNumerador())
print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)
print(numero1 == numero2)
print(numero1 != numero2)
print(numero1 < numero2)
print(numero1 <= numero2)
print(numero1 > numero2)
print(numero1 >= numero2)
print(numero1)
print(numero2)

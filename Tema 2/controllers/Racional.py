"""
Donde se usa:
2.4.py

"""

class Racional():
    numerador = 0
    denominador = 0

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def getNumerador(self):
        return self.numerador

    def getDenominador(self):
        return self.denominador

    def setNumerador(self, numerador):
        self.numerador = numerador

    def setDenominador(self, denominador):
        self.denominador = denominador

    def mcd(self, m, n):
        while m % n != 0:
            mViejo = m
            nViejo = n
            m = nViejo
            n = mViejo % nViejo
        return n

    def cambioSigno(self):
        if (self.numerador > 0 and self.denominador > 0) or (self.numerador < 0 and self.denominador < 0):
            self.numerador = abs(self.numerador)
            self.denominador = abs(self.denominador)
        else:
            self.numerador = -abs(self.numerador)
            self.denominador = -abs(self.denominador)


    def __add__(self, objeto):
        resultadoNum = self.numerador*objeto.getDenominador() + self.denominador * \
            objeto.getNumerador()
        resultadoDen = self.denominador*objeto.denominador
        divisor = self.mcd(resultadoNum, resultadoDen)
        return Racional(resultadoNum//divisor, resultadoDen//divisor)

    def __sub__(self, objeto):
        resultadoNum = self.numerador*objeto.getDenominador() - self.denominador * \
            objeto.getNumerador()
        resultadoDen = self.denominador*objeto.denominador
        divisor = self.mcd(resultadoNum, resultadoDen)
        return Racional(resultadoNum//divisor, resultadoDen//divisor)

    def __mul__(self, objeto):
        resultadoNum = self.numerador*objeto.getDenominador() * self.denominador * \
            objeto.getNumerador()
        resultadoDen = self.denominador*objeto.denominador
        divisor = self.mcd(resultadoNum, resultadoDen)
        return Racional(resultadoNum//divisor, resultadoDen//divisor)

    def __truediv__(self, objeto):
        resultadoNum = self.numerador*objeto.getDenominador() // self.denominador * \
            objeto.getNumerador()
        resultadoDen = self.denominador*objeto.denominador
        divisor = self.mcd(resultadoNum, resultadoDen)
        return Racional(resultadoNum//divisor, resultadoDen//divisor)

    def __eq__(self, objeto):
        if not objeto:
            return False
        return self.numerador == objeto.numerador and self.denominador == objeto.denominador

    def __ne__(self, objeto):
        return not self == objeto

    def __lt__(self, objeto):
        if not objeto:
            return False
        return self.numerador < objeto.numerador and self.denominador < objeto.denominador

    def __le__(self, objeto):
        if not objeto:
            return False
        return self.numerador <= objeto.numerador and self.denominador <= objeto.denominador

    def __gt__(self, objeto):
        if not objeto:
            return False
        return self.numerador > objeto.numerador and self.denominador > objeto.denominador

    def __ge__(self, objeto):
        if not objeto:
            return False
        return self.numerador >= objeto.numerador and self.denominador >= objeto.denominador

    def __str__(self):
        return (str(self.numerador)+"/"+str(self.denominador))

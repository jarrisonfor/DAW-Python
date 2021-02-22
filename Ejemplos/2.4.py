class Fraccion():
    def __init__(self, numerador, denominador):
        self.__num = numerador
        self.__den = denominador

    def devolvernum(self):
        return self.__num

    def establecernumerador(self, numerador):
        self.__num = numerador;

    def establecerdenominador(self,denominador):
        self.__den = denominador

    def devolverden(self):
        return self.__den

    def mcd(self,m, n):
        while m % n != 0:
            mViejo = m
            nViejo = n
            m = nViejo
            n = mViejo % nViejo
        return n

    def __str__(self):
        return (str(self.__num)+"/"+str(self.__den))

    def __add__(self, objeto): # Sobrecarga del operador +

        resultado = Fraccion(0,0)
        resnum = self.__num*objeto.devolverden() + self.__den*objeto.devolvernum()
        resden = self.__den*objeto.__den
        divisor = self.mcd(resnum, resden)
        resultado.establecernumerador(resnum//divisor)
        resultado.establecerdenominador(resden//divisor)
        return resultado

    def __sub__(self, objeto): # Sobrecarga del operador -

        resultado = Fraccion(0,0)
        resnum = self.__num*objeto.devolverden() - self.__den*objeto.devolvernum()
        resden = self.__den*objeto.__den
        divisor = self.mcd(resnum, resden)
        resultado.establecernumerador(resnum//divisor)
        resultado.establecerdenominador(resden//divisor)

        return resultado

# Programa principal

numero1 = Fraccion(5,4)
numero2 = Fraccion(3,5)

suma = Fraccion(0,0)
resta = Fraccion(0,0)

suma = numero1 + numero2
resta = numero1 - numero2

print("La suma es",suma)
print("La resta es",resta)

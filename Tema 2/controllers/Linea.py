"""
Donde se usa:
A-2.1.py

"""

from .Punto import Punto
from math import sqrt

class Linea:

    def __init__(self, p1=Punto(0,0), p2=Punto(0,0)):
        self.p1 = p1
        self.p2 = p2

    def cambiarPunto1(self, p1):
        self.p1 = p1

    def cambiarPunto2(self, p2):
        self.p2 = p2

    def devolverPunto1(self):
        return self.p1

    def devolverPunto2(self):
        return self.p2

    def __str__(self):
        return "["+str(self.p1)+str(self.p2)+"]"+"\nDistancia "+str("{0:.2f}".format(self.distancia()))

    def distancia(self):
        return sqrt((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2)

    def puntocercano(self):
        distanciaP1= sqrt(self.p1.x ** 2 + self.p1.y ** 2)
        distanciaP2= sqrt(self.p2.x ** 2 + self.p2.y ** 2)
        if distanciaP1 < distanciaP2:
            return self.p1
        else:
            return self.p2
"""
Donde se usa:
2.1.py

"""

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def IntroduceX(self, x):
        self.x = x

    def IntroduceY(self, y):
        self.y = y

    def Muestra_puntoX(self):
        return self.x

    def Muestra_puntoY(self):
        return self.y

    def __str__(self):
        return "("+str(self.x) +", "+ str(self.y)+")"

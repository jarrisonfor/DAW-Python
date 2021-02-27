"""
Donde se usa:
2.10.py
"""
import datetime
from controllers.Bombilla import Bombilla

class Casa:
    bombillas = []
    interruptorGeneral = False

    def __init__(self, interruptorGeneral = False):
        self.interruptorGeneral = interruptorGeneral

    def getBombillas(self):
        c = 0
        for bombilla in self.bombillas:
            if self.interruptorGeneral:
                print(f"{c}. {bombilla}")
            else:
                print(f"{c}. Estado: False")
            c += 1
        print("\n")

    def addBombilla(self, bombilla):
        if isinstance(bombilla, Bombilla):
            self.bombillas.append(bombilla)
        else:
            print('Eso no es una bombilla.')

    def switchInterruptor(self):
        self.interruptorGeneral = not self.interruptorGeneral

    def switchBombilla(self, bombilla):
        try:
            self.bombillas[bombilla].switchEncendido()
        except:
            print('Elige un numero de bombilla correcto')

    def bajaIntensidadBombilla(self, bombilla):
        try:
            self.bombillas[bombilla].bajarIntensidad()
        except:
            print('Elige un numero de bombilla correcto')

    def subirIntensidadBombilla(self, bombilla):
        try:
            self.bombillas[bombilla].subirIntensidad()
        except:
            print('Elige un numero de bombilla correcto')

    def __str__(self):
        return f"Bombillas: {len(self.bombillas)}"

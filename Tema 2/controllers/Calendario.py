"""
Donde se usa:
2.5.py

"""
import datetime

class Calendario:
    date = None
    dia = None
    mes = None
    anho = None

    def __init__(self, dia=None, mes=None, anho=None):
        try:
            self.date = datetime.datetime(anho, mes, dia)
        except:
            self.date = datetime.datetime.now()
        self.dia = self.date.day
        self.mes = self.date.month
        self.anho = self.date.year

    def Calendario(self, dia=None, mes=None, anho=None):
        return Calendario(dia, mes, anho)

    def incrementarDia(self, cantidad):
        self.date = self.date + datetime.timedelta(days=int(cantidad))
        self.dia = self.date.day

    def incrementarMes(self, cantidad):
        self.date = self.date.replace(year=(self.date.year + ((self.date.month + cantidad) // 12)), month=((self.date.month + int(cantidad)) % 12))
        self.mes = self.date.month

    def incrementarAnho(self, cantidad):
        self.date = self.date.replace(year=(self.date.year + int(cantidad)))
        self.anho = self.date.year

    def __eq__(self, other):
        if isinstance(other, Calendario):
            if other.dia == self.dia and other.mes == self.mes and other.anho == self.anho:
                return True
        return False

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anho}"

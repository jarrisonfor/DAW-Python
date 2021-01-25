"""
Donde se usa:
A-2.5.py

"""
import datetime

class Hora:
    hour = 0
    minute = 0
    second = 0
    def __init__(self, hora, segundos):
        horaSeparada = hora.split(':');
        self.date = datetime.datetime.now()
        try:
            self.setHora(horaSeparada[0])
            self.setMinuto(horaSeparada[1])
            self.setSegundo(horaSeparada[2])
        except:
            print('No se ha introducido un formato de hora correcto, se usara la hora actual')
        self.incrementaSegundo(segundos)

    def setHora(self, hora):
        try:
            self.date = self.date.replace(hour=int(hora))
        except:
            pass
        self.hour = self.date.hour
    def getHora(self):
        return self.hour


    def setMinuto(self, minuto):
        try:
            self.date = self.date.replace(minute=int(minuto))
        except:
            pass
        self.minute = self.date.minute
    def getMinuto(self):
        return self.minute


    def setSegundo(self, segundo):
        try:
            self.date = self.date.replace(second=int(segundo))
        except:
            pass
        self.second = self.date.second
    def getSegundo(self):
        return self.second


    def incrementaSegundo(self, segundo):
        try:
            self.date = self.date + datetime.timedelta(seconds=int(segundo))
            self.setHora(self.date.hour)
            self.setMinuto(self.date.minute)
            self.setSegundo(self.date.second)
        except:
            self.date = self.date + datetime.timedelta(seconds=0)

    def __str__(self):
        return f"Hora: {self.getHora()}:{self.getMinuto()}:{self.getSegundo()}"

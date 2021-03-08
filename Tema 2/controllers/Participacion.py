"""
Donde se usa:
2.9.py
"""

class Participacion:
    def __init__(self, actor, pelicula, papelPrincipal):
        self.actor = actor
        self.pelicula = pelicula
        self.papelPrincipal = papelPrincipal
        actor.addParticipacion(self)
        pelicula.addParticipacion(self)


    def getActor(self):
        return self.actor
    def getPelicula(self):
        return self.pelicula

    def setActor(self, actor):
        self.actor = actor
    def setPelicula(self, pelicula):
        self.pelicula = pelicula


    def __str__(self):
        return f"Participacion: el actor {self.actor.getNombre()} participa en la pelicula {self.pelicula.getTitulo()}"

    @staticmethod
    def saveParticipacionDb(self):
        pass
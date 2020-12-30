"""
Donde se usa:
A-2.3.py

"""


class ConjuntoLibros:
    conjunto = []
    sizeLimit = 10

    def __init__(self, sizeLimit=10):
        self.sizeLimit = sizeLimit

    def addLibro(self, libro):

        if self.getLibro(libro.titulo):
            return False

        if len(self.conjunto) < self.sizeLimit:
            self.conjunto.append(libro)
            return True
        return False

    def delLibro(self, titulo='', autor=''):
        self.conjunto = [i for i in self.conjunto if i.titulo != titulo]
        self.conjunto = [i for i in self.conjunto if i.autor != autor]

    def getTopBottom(self):
        max = 0
        libroMax = ''
        min = 10
        libroMin = ''
        for i in self.conjunto:
            if i.calificacion > max:
                max = i.calificacion
                libroMax = i
            if i.calificacion < min:
                min = i.calificacion
                libroMin = i
        return [libroMax.titulo, libroMin.titulo]

    def getLibro(self, titulo):
        try:
            return [i for i in self.conjunto if i.titulo == titulo][0]
        except:
            return False

    def __str__(self):
        return f"conjunto: {self.conjunto}\nsizeLimit: {self.sizeLimit}\n"

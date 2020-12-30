"""
Donde se usa:
A-2.3.py

"""


class Libro:
    titulo = ''
    autor = ''
    paginas = 0
    calificacion = 5

    def __init__(self, titulo, autor, paginas, calificacion=5):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.calificacion = calificacion

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getPaginas(self):
        return self.paginas

    def getCalificacion(self):
        return self.calificacion

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setAutor(self, autor):
        self.autor = autor

    def setPaginas(self, paginas):
        self.paginas = paginas

    def setCalificacion(self, calificacion):
        self.calificacion = calificacion

    def __str__(self):
        return f"titulo: {self.titulo}\nautor: {self.autor}\npaginas: {self.paginas}\ncalificacion: {self.calificacion}\n"

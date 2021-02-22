class Error(Exception):
    def __init__(self, mensaje="Se ha producido un error"):
        self.mensaje = mensaje

    def __str__(self):
        return str(self.mensaje)
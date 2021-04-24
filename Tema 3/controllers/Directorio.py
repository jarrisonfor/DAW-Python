from controllers.Archivo import Archivo
from controllers.Nodo import Nodo
import re



class Directorio(Nodo):

    # Un fichero puede ser un archivo o un directorio
    # Nodo del árbol denominado archivo que hereda de fichero
    # Le pasamos el nombre al contructor de su padre
    # Los directorios contienen una lista de archivos (Ficheros y Directorios)

    def __init__(self, nombre):
        super(Directorio, self).__init__(nombre)
        # Llamamos al contructor del padre
        self.Nodos = []
        # Lista de archivos y directorios en su interior

    # Mediante esta sobrecarga devolvemos la información del fichero como cadena de caracteres.
    # De esta forma, permitimos hacer print(nombreobjeto)
    # Imprimimos los atributos comunes heredados de nuestro padre y le concatenamos los propios.
    def __str__(self):
        return super(Directorio, self).__str__() + "\nLista Hijos: " + self.imprimirContenidoDirectorio()

    def imprimirContenidoDirectorio(self):
        cadena = "{"
        if len(self.Nodos) != 0:
            for fichero in self.Nodos:
                cadena += str(fichero.getNombre())+","
        cadena += "}"
        return cadena

    def buscarNodos(self, nombre):
        if len(self.Nodos) != 0:
            for fichero in self.Nodos:
                if fichero.getNombre() == nombre:
                    return fichero
        return None

    def nuevaCarpeta(self, nombre):
        nuevoDir = self.buscarNodos(nombre)
        if nuevoDir != None:
            print("La carpeta ya existe")
        else:
            nuevoDir = Directorio(nombre)
            nuevoDir.setPadre(self)
            self.Nodos.append(nuevoDir)
        return nuevoDir

    def borrarCarpeta(self, nombre):
        directorio = self.buscarNodos(nombre)
        if directorio == None:
            print("La carpeta no existe")
        else:
            if len(directorio.Nodos) > 0:
                print("La carpeta no esta vacia")
            else:
                self.Nodos.remove(directorio)

    def nuevoArchivo(self, nombre):
        nuevoFich = self.buscarNodos(nombre)
        if nuevoFich != None:
            print("El fichero ya existe")
        else:

            nuevoFich = Archivo(nombre)
            nuevoFich.setPadre(self)
            self.Nodos.append(nuevoFich)
        return nuevoFich

    def borrarArchivo(self, nombre, opcion = ''):
        fichero = self.buscarNodos(nombre)
        if fichero != None and isinstance(fichero, Archivo):
            self.Nodos.remove(fichero)
        elif isinstance(fichero, Directorio) and opcion == '-R':
            self.Nodos.remove(fichero)
        elif isinstance(fichero, Directorio):
            print("las carpetas no se pueden sin la opcion -R")
        elif isinstance(fichero, Directorio):
            print("El fichero no existe")

    def preorden(self, nodo, j):
        if nodo == None:
            return ""
        print(("\t"*j) + nodo.getNombre())
        if isinstance(nodo, Directorio):
            for i in range(len(nodo.Nodos)):
                self.preorden(nodo.Nodos[i], j+1)

    def findFile(self, nodo, j, nombre, ruta = '/'):
        if nodo == None:
            return ""
        if nodo.getNombre() == nombre and isinstance(nodo, Archivo):
            absoluta = ruta + nodo.getNombre()
            print(re.sub(r'^\/*', '/', absoluta))
        if isinstance(nodo, Directorio):
            for i in range(len(nodo.Nodos)):
                self.findFile(nodo.Nodos[i], j+1, nombre, ruta + nodo.getNombre() + '/')

    def renombrarArchivo(self, nombreViejo, nombreNuevo):
        fichero = self.buscarNodos(nombreViejo)
        if fichero != None:
            if isinstance(fichero, Archivo):
                fichero.setNombre(nombreNuevo)
            else:
                print("No se puede renombrar una carpeta")
        else:
            print("El fichero no existe, no se puede renombrar")

    def escribirFichero(self, nombre, datos):
        fichero = self.buscarNodos(nombre)
        if fichero != None:
            if isinstance(fichero, Archivo):
                fichero.setContenido(datos)
            else:
                print("No se puede escribir datos en una carpeta")
        else:
            print("El fichero no existe")
    
    def copiarArchivo(self, file):
        fichero = self.buscarNodos(file.getNombre())
        if fichero != None:
            print("El fichero ya existe")
        else:
            self.Nodos.append(file)
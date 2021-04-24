from controllers.Directorio import Directorio
from controllers.Archivo import Archivo
import os


class SistemaFicheros():

    # Un sistema de ficheros es un árbol (conjunto de nodos de tipo archivo y directorio)
    # Le pasamos el nodo raiz al contructor de su padre

    def __init__(self, raiz):
        self.__root = raiz
        # Nodo raiz del árbol (colgarán el resto de los nodos)
        self.__pwd = raiz
        # Nodo que representa el directorio actual del árbol (inicialmente raiz).

    # Devuelve el nodo raiz del árbol
    def getRoot(self):
        return self.__root

    # Devuelve el directorio actual de trabajo.
    def getPwd(self):
        return self.__pwd

    # Devuelve la ruta actual desde la raiz.
    def imprimirRutaActual(self):
        aux = self.__pwd
        cadena = ""
        while aux != None:
            if aux.getNombre() != "/":
                # Si no estamos en el raiz.
                cadena = aux.getNombre()+"/"+cadena
            else:
                # Si estamos en el raiz evitamos duplicar barra
                cadena = aux.getNombre() + cadena
            aux = aux.getPadre()
        return cadena

    def listarDirectorioRecursivo(self):
        self.__pwd.preorden(self.__pwd, 0)

    def listarContenidoDirectorio(self):
        print(self.__pwd.imprimirContenidoDirectorio())

    def listarArchivo(self, nombre):
        archivobuscado = self.__pwd.buscarNodos(nombre)
        if archivobuscado != None and isinstance(archivobuscado, Archivo):
            # Si se ha encontrado el archivo y no es un directorio
            print(archivobuscado)
        else:
            print("No existe como archivo", archivobuscado)

    def cambiarDirectorio(self, nombredir):
        if nombredir == '..':
            # Si no es el directorio raiz
            if self.__pwd.getPadre() != None:
                # Si es "cd .." volvemos al directorio padre
                # Cambiamos el directorio actual de trabajo
                self.__pwd = self.__pwd.getPadre()
            else:
                print("Está usted en el directorio raiz")
        else:
            # Si es un nombre de directorio
            dirbuscado = self.__pwd.buscarNodos(nombredir)
            if dirbuscado != None and isinstance(dirbuscado, Directorio):
                self.__pwd = dirbuscado
            else:
                print("No existe como directorio ", nombredir)

    def crearDirectorio(self, nombredir):
        dirbuscado = self.__pwd.buscarNodos(nombredir)
        if dirbuscado == None:
            self.__pwd.nuevaCarpeta(nombredir)
        else:
            print("El directorio ya existe")

    def crearArchivo(self, nombrearchivo):
        archivobuscado = self.__pwd.buscarNodos(nombrearchivo)
        if archivobuscado == None:
            self.__pwd.nuevoArchivo(nombrearchivo)
        else:
            print("El fichero ya existe")

    def borrarArchivo(self, nombrearchivo, opcion = ''):
        archivobuscado = self.__pwd.buscarNodos(nombrearchivo)
        if archivobuscado == None:
            print("El fichero no existe")
        else:
            self.__pwd.borrarArchivo(nombrearchivo, opcion)

    def borrarDirectorio(self, nombredir):
        dirbuscado = self.__pwd.buscarNodos(nombredir)
        if dirbuscado == None:
            print("El directorio no existe")
        else:
            self.__pwd.borrarCarpeta(nombredir)

    def encontrarNodo(self, nombre):
        self.__pwd.findFile(self.__root, 0, nombre)

    def renombrarFichero(self, nombreold, nombrenew):
        archivobuscado = self.__pwd.buscarNodos(nombreold)
        if archivobuscado == None:
            print("El fichero no existe, no se puede renombrar")
        else:
            self.__pwd.renombrarArchivo(nombreold, nombrenew)

    def copiarFichero(self, nombrearchivo, rutacopia):
        archivobuscado = self.__pwd.buscarNodos(nombrearchivo)
        if archivobuscado == None:
            print("El fichero no existe")
        else:
            rutaArray = rutacopia.split('/')
            tmpActual = self.__pwd
            self.__pwd = self.__root
            for i in rutaArray:
                if i != "":
                    self.cambiarDirectorio(i)
            self.__pwd.copiarArchivo(archivobuscado)
            self.__pwd = tmpActual

    def moverFichero(self, nombrearchivo, rutanueva):
        archivobuscado = self.__pwd.buscarNodos(nombrearchivo)
        if archivobuscado == None:
            print("El fichero no existe")
        else:
            self.borrarArchivo(archivobuscado.getNombre())
            rutaArray = rutanueva.split('/')
            tmpActual = self.__pwd
            self.__pwd = self.__root
            for i in rutaArray:
                if i != "":
                    self.cambiarDirectorio(i)
            self.__pwd.copiarArchivo(archivobuscado)
            self.__pwd = tmpActual

    def escribirFichero(self, nombre, datos):
        archivobuscado = self.__pwd.buscarNodos(nombre)
        if archivobuscado == None:
            print("El fichero no existe")
        else:
            self.__pwd.escribirFichero(nombre, " ".join(datos))

    # AÑADIDO - Limpiar el terminal
    def limpiarTerminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
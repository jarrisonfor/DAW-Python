"""
UT2-AEA3 Colección de libros
Queremos mantener una colección de los libros que hemos ido leyendo, poniéndoles una calificación según nos haya gustado más o menos al leerlo.

Para ello, crear la clase Libro, cuyos atributos son:
el título
el autor
el número de páginas
la calificación que le damos entre 0 y 10.

Crear los métodos típicos para poder modificar y obtener los atributos si tienen sentido.

Posteriormente, crear una clase ConjuntoLibros, que almacena un conjunto de libros (con un array de un tamaño fijo).

Se pueden añadir libros que no existan (siempre que haya espacio)
eliminar libros por título o autor
mostrar por pantalla los libros con la mayor y menor calificación dada
mostrar un contenido de todo el conjunto.

En el programa principal realizar varias pruebas con las clases creadas. En concreto, pruebe a:
crear dos libros
añadirlos a la lista
eliminarlos por los dos criterios hasta que la lista esté vacía
volver a añadir un libro
mostrar el contenido final.
"""

from controllers.Libro import Libro
from controllers.ConjuntoLibros import ConjuntoLibros


libro1 = Libro('libro1', 'yo', 300, 10)
libro2 = Libro('libro2', 'el', 400, 2)
libro3 = Libro('libro2', 'yo', 400, 2)
print(libro1)
print(libro2)

conjunto1 = ConjuntoLibros(5)
print(conjunto1)

conjunto1.addLibro(libro1)
conjunto1.addLibro(libro2)
conjunto1.addLibro(libro3)
print(conjunto1)

print(conjunto1.getLibro('libro1'))
print(conjunto1.getLibro('libro2'))
print(conjunto1.getTopBottom())
print('\n')

conjunto1.delLibro('libro2')
print(conjunto1)

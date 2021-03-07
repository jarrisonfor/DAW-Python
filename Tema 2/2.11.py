"""
UT2-AE0. Agenda carnaval de Arrecife
1º) El ayuntamiento de Arrecife nos ha solicitado implementar una clase en su aplicación Python denominada “AgendaCarnaval” que representa los eventos del carnaval de este año.
Los datos necesarios que necesitará dicha clase son: fecha del evento, lugar, nombre del evento, descripción del evento y ruta de una imagen que representa el evento.

Ejemplo:

Fecha: 31/01/2019
Lugar: Recinto Ferial
Nombre: Concurso de Murgas Infantil
Descripción: Desarrollo de la fase 1 del concurso de murgas infantil.
Imagen: http://www.arrecife.es/portal/fotoEvento01.png
Las acciones que podemos controlar en esta clase son:

a) Definir todos los atributos de la clase como privados.

b) Crear un constructor sin parámetros para crear evento por defecto.
Al crear un nuevo evento el atributo fecha tendrá la fecha del sistema al crear el objeto.
El atributo lugar indicará por defecto el valor “Recinto Ferial”.

c)Sobrecargar el constructor de crear eventos, donde le pase por parámetro todos los atributos necesarios de la clase.

d)Definir todos los métodos get y set de los atributos.
Desarrolla además desde la clase principal main, pruebas para ver el funcionamiento de la clase.

Debes crear 4 eventos con fechas distintas.
Debes mostrar en pantalla cada uno de dichos eventos con todos sus atributos, una vez creados.
Debes crear un método en el main que permita modificar los atributos de alguno de los eventos creados.
Puntuación: 6 puntos sí está completo, funciona, está comentado y existe control de excepciones.

2º) Desarrolla un método en la clase “AgendaCarnaval” que permita saber cuántos días han transcurrido entre un evento y otro.
Ejemplo:

Evento 1 fecha: 31/01/2019;

Evento 2 fecha: 01/02/2019;

Resultado: “Ha transcurrido 1 día entre el evento 1 y el evento 2”

Muestra desde la clase principal main, el funcionamiento de este método.
Puntuación: 2 puntos sí está completo, funciona, está comentado y existe control de excepciones.

3º) Desarrolla un método en la clase “AgendaCarnaval” que permita limitar el atributo descripción a 50 caracteres.
Sí el atributo descripción tiene más de 50 caracteres, se eliminará el resto de caracteres.

Ejemplo:

Descripción: “Esto es una prueba para comprobar que tengo más de 50 caracteres en el atributo descripción”;

Resultado: “Esto es una prueba para comprobar que tengo más ”.

Muestra desde la clase principal main, el funcionamiento de este método, indicando además al usuario que ha superado el límite del atributo.

Puntuación: 2 puntos sí está completo, funciona, está comentado y existe control de excepciones.

Nota: Para valorar dicho examen se debe subir a la Moodle el proyecto creado
"""
from datetime import datetime

from controllers.AgendaCarnaval import AgendaCarnaval

evento1 = AgendaCarnaval('canaryfest', 'fiestaus fiestaus fiestaus', 'imagenpng')
evento2 = AgendaCarnaval('canaryfest2', 'fiestaus2 fiestaus2 fiestaus2', 'imagenpng2', 'costa teguise', datetime(2021, 3, 9))
evento3 = AgendaCarnaval('canaryfest3', 'fiestaus3 fiestaus 3fiestaus', 'imagenpng3', 'haria', datetime(2021, 4, 1))
evento4 = AgendaCarnaval('canaryfest4', 'fiestaus4 fiestaus t4akus', '4imagenpng4', 'la graciosa', datetime(2021, 5, 1))


print(evento1)
print(evento2)
print(evento3)
print(evento4)

evento1.setNombre('lanzaroteFest')
evento2.setNombre('lanzaroteFest2')
evento3.setNombre('lanzaroteFest3')
evento4.setNombre('lanzaroteFest4')
print()

print(evento1)
print(evento2)
print(evento3)
print(evento4)


print(evento1.calcularFecha(evento2.getFecha()))


print()

evento1.setDescripcion('Esto es una prueba para comprobar que tengo más de 50 caracteres en el atributo descripción')

print(evento1.getDescripcion())

"""
UT5-AE1. Diagrama de clases UML.

Cadena de Videoclubs
Una cadena de videoclubs ha decidido emplear un sistema de información para almacenar la información referente a las películas que ofrece en alquiler.

Está información es la que se detalla a continuación:

Una película se caracteriza por su título, nacionalidad, productora y fecha.
En una película pueden participar varios actores con nombre artístico, nacionalidad, sexo y siendo algunos de ellos actores principales (True / False).
Una película puede estar dirigida por un único director con nombre artístico, nacionalidad, sexo y género cinematográfico.

Un director puede dirigir muchas películas.
De cada película se dispone de uno o varios ejemplares diferenciados por un número de ejemplar y caracterizados por su estado de conservación.

Cada ejemplar estará asociado a una única película y su existencia depende de esta última.
Un ejemplar se puede encontrar alquilado a un único socio con dni, nombre, apellido, dirección y teléfono.

Se desea almacenar la fecha de comienzo del alquiler y la de devolución en el alquiler.
Un socio tiene que ser avalado por otro socio que responda de él en caso de existir algún tipo de problema (relación reflexiva, recursiva o unaria).


1. Diseñar el Diagrama de Clases del Diseño UML empleando alguna herramienta (por ejemplo DIA)
2. Pasar a la fase de Codificación (Clases en Python) a partir del Diseño (Diagrama de Clases UML)
"""

from pathlib import Path

from controllers.Actor import Actor
from controllers.Socio import Socio
from controllers.Director import Director
from controllers.Pelicula import Pelicula
from controllers.Alquiler import Alquiler
from controllers.Ejemplar import Ejemplar
from controllers.Participacion import Participacion

databasePath = Path(__file__).parent / "database"

Socio.resetSocioDb(databasePath)


aval = Socio('española', 'pepe', 'perez', 'calle inventada 2', '12345679Z', '928123416', 'masculino')
director1 = Director('española', 'juan', 'perez', 'calle inventada', '12345678Z', '928123456', 'masculino', 'Oda', 'suspense')
actor1 = Actor(director1.getNacionalidad(), director1.getNombre(), director1.getApellido(), director1.getDireccion(), director1.getDni(), director1.getTelefono(), director1.getSexo(), 'L')
socio1 = Socio(actor1.getNacionalidad(), actor1.getNombre(), actor1.getApellido(), actor1.getDireccion(), actor1.getDni(), actor1.getTelefono(), actor1.getSexo())
pelicula1 = Pelicula('Death note', 'Inglesa', 'La productora', '01/10/2022', director1)
ejemplar1 = Ejemplar('1', 'Perfecto', pelicula1)

participacion1 = Participacion(actor1, pelicula1, True)
alquiler1 = Alquiler(socio1, ejemplar1, aval, '01/10/2022', '03/10/2022')

Socio.saveSocioDb(socio1, databasePath)
Director.saveDirectorDb(director1, databasePath)
Actor.saveActorDb(actor1, databasePath)
Pelicula.savePeliculaDb(pelicula1, databasePath)
""" Ejemplar.saveEjemplarDb(ejemplar1)
Participacion.saveParticipacionDb(participacion1)
Alquiler.saveAlquilerDb(alquiler1) """



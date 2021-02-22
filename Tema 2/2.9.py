"""
UT5-AE1. Diagrama de clases UML. Cadena de Videoclubs
Una cadena de videoclubs ha decidido emplear un sistema de información para almacenar la información referente a las películas que ofrece en alquiler. Está información es la que se detalla a continuación:

Una película se caracteriza por su título, nacionalidad, productora y fecha.
En una película pueden participar varios actores con nombre artístico, nacionalidad, sexo y siendo algunos de ellos actores principales (True / False).
Una película puede estar dirigida por un único director con nombre artístico, nacionalidad, sexo y género cinematográfico. Un director puede dirigir muchas películas.
De cada película se dispone de uno o varios ejemplares diferenciados por un número de ejemplar y caracterizados por su estado de conservación. Cada ejemplar estará asociado a una única película y su existencia depende de esta última.
Un ejemplar se puede encontrar alquilado a un único socio con dni, nombre, apellido, dirección y teléfono. Se desea almacenar la fecha de comienzo del alquiler y la de devolución en el alquiler.
Un socio tiene que ser avalado por otro socio que responda de él en caso de existir algún tipo de problema (relación reflexiva, recursiva o unaria).
1. Diseñar el Diagrama de Clases del Diseño UML empleando alguna herramienta (por ejemplo DIA)

2. Pasar a la fase de Codificación (Clases en Python) a partir del Diseño (Diagrama de Clases UML)
"""


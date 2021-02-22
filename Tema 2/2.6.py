"""
UT3-AEA6 Diagrama de clases UML - Proyecto gestión de un instituto
DIAGRAMA DE CLASES UML

Se desea informatizar la gestión de un centro integrado de formación profesional.

En este centro educativo encontramos profesores y alumnos.
De estas personas se almacenará su DNI, nombre, apellidos, dirección y teléfono.

guardaremos el vínculo de los profesores y la especialidad a la que pertenecen.

De las personas que son alumnos guardaremos también el número de expediente y la fecha de nacimiento.

Los profesores imparten módulos y cada módulo tiene un código y un nombre.

Los profesores pueden impartir varios módulos, pero un módulo sólo puede ser impartido por un profesor.

Cada alumno tendrá una o varias matrículas identificadas por un código e incluirá cada una de ellas el curso académico correspondiente.

Un alumno puede tener asociados varias matrículas (una por curso académico).

La matrícula depende del alumno y por lo tanto, no puede existir sin él.

Además, de cada matrícula se guarda "detalles" o "líneas de matrícula" donde se indican los módulos que componen la matrícula y la calificación obtenida en cada uno de ellos.

La línea de matrícula depende de la matrícula y por lo tanto, no puede existir sin la matrícula.

1. Diseñar el Diagrama de Clases del Diseño UML

2. Pasar a la fase de Codificación (Clases en Python) a partir del Diseño (Diagrama de Clases UML)

3. Realizar las operaciones (métodos) que se detallan a continuación:  (se describirán más adelante...)

https://online.visual-paradigm.com/app/diagrams/

"""


import sqlite3
conn = sqlite3.connect('./database/sqlite.db')


c = conn.cursor()
""" c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''') """
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchall())

conn.commit()
conn.close()

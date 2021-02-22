"""
Preparación del examen

Para la realización del examen es necesario utilizar fechas. Para representar fechas en Python
utilizaremos las clases que vienen incluidas en la biblioteca Datetime.
Importante: lee todo el enunciado antes de comenzar a programar la aplicación. Te puede resultar
útil preparar en papel un esquema de la aplicación antes de comenzar a programarla.
Queremos desarrollar una aplicación para la gestión de matrículas y expedición de títulos de cursos
organizados por una academia de formación.
Un alumno representa la persona que puede realizar un curso. Un alumno se caracteriza por tener
un nombre, dni y un saldo disponible (dinero para el pago de los cursos). Los atributos nombre y
dni se pasan la primera vez al constructor y no se pueden volver a cambiar. El saldo se puede
modificar utilizando dos operaciones: una que incremente el saldo y otra que lo decremente en una
cantidad. El saldo disponible puede establecerse de manera opcional en el constructor. Por defecto,
el valor inicial será de 100 euros. Además, el alumno debe mantener la información de los cursos
que ha realizado y de los que está matriculado actualmente. Ambas listas se pueden consultar.
También se puede consultar si el alumno ha realizado o está matriculado de un curso concreto
(métodos de búsqueda en listas).
Un curso se caracteriza por las siguientes propiedades:
- Título.
- Fecha de inicio del curso.
- Fecha de finalización del curso.
- Número de días.
- Número de horas por día
- Precio.
- Alumnos matriculados. Lista de alumnos que se han matriculado del curso.
- Número de alumnos matriculados.
El título, las fechas de inicio y finalización, los días de clase, el número de horas por día y el precio
se establecen en el constructor y no pueden cambiar. Todas las propiedades se pueden consultar. De
forma general, un alumno podrá matricularse en un curso si tiene saldo suficiente para afrontar el
pago. En el caso de que se haya realizado la matrícula, el alumno formará parte de los alumnos
matriculados del curso, el saldo del alumno tendrá que haberse actualizado y el curso quedará
registrado en la lista/colección de cursos en los que está matriculado el alumno. Por último, se debe
informar si el alumno ha podido matricularse o no.
Una vez concluido el curso, podrá expedirse el título para cada alumno. Por tanto, esta operación
recibe como parámetro el alumno al que se va a expedir el título. Los requisitos para la expedición
del título de un alumno son los siguientes:
1. Que el curso haya terminado.
2. Que el alumno esté matriculado.
3. Que no se haya gestionado todavía la expedición del título para este alumno (el curso no está
en la lista de cursos realizados del alumno).
Si se cumplen estas condiciones, el curso pasará de la lista de cursos matriculados del alumno a la
lista de cursos realizados y se devuelve una cadena de texto a modo de diploma. En caso de no
cumplir los requisitos se devolverá None.
La información del diploma será:
D/Dª nombreAlumno ha realizado con aprovechamiento el curso títuloCurso, en la modalidad
tipoCurso, con una duración de medidaTiempo horas.
Para la expedición del título se considera que medidaTiempo se corresponde con el número de días
multiplicado por el número de horas establecidas en su construcción y que por simplicidad de la
aplicación siempre se superan estos cursos con aprovechamiento (por simplicidad, no vamos a
implementar mecanismos de control de asistencia).
La información de tipoCurso depende del tipo de curso en el que se haya matriculado el alumno,
tal y como se verá en las siguientes líneas:
Existen dos tipos de cursos: presencial y online. Un curso online puede tener prerequisitos para su
matriculación que consisten en una lista de cursos que ha tenido que realizar el alumno
previamente. Estos prerrequisitos se establecen en el constructor y no pueden cambiar. De esta
forma, si existen prerequisitos para matricular a un alumno en un curso online, tendrá que cumplir
las condiciones generales de matriculación (relativas al pago) y además haber realizado los cursos
establecidos como prerrequisitos.
Los atributos que caracterizan un curso presencial son:
• Cupo. Número máximo de alumnos que pueden matricularse del curso
• Plazas libres: número de alumnos que aún pueden matricularse en el curso, esto es, el cupo
menos el número de alumnos matriculados.
El cupo se establece en la construcción y no se puede cambiar. En un curso presencial sólo podrá
matricularse un alumno si, cumpliendo las condiciones generales de matriculación, quedan plazas
libres, es decir, si no se ha alcanzado el cupo.


1. (6,5 puntos) El ejercicio consiste en programar los tipos de datos necesarios para implementar
esta aplicación. En este apartado se valorarán los siguientes puntos:
• El diseño de las clases (1 punto)
• Implementación de mecanismos de herencia (1,50 puntos)
• El uso de listas/colecciones. (1,50 puntos)
• El manejo de fechas. (1 punto)
• El polimorfismo en los métodos. (1,5 puntos)

2. (2,5 puntos) La redefinición de métodos, la sobrecarga de operadores (1,5 puntos) y el manejo
de excepciones (1 punto) se valorará llevando a cabo las implementaciones que se indican a
continuación:
• Redefinir el método __str__ en la clase Alumno. Al utilizar print sobre cualquier objeto de
tipo alumno se imprimirá la información relativa a este: nombre dni, saldo, nombre de los
cursos realizados y nombre de los cursos matriculados.
• Crea una clase Error que herede de la clase Excepcion() con la que produciremos nuestras
propias excepciones. Implementa mecanismos en dos métodos para la captura y el manejo
de estas excepciones generadas.
• Declara un método en los cursos que retorne un listado ordenado de alumnos matriculados
por DNI haciendo uso del método sort() existente en la clase lista. El método sort() puede
tener parametrizado el criterio de ordenación o puedes optar por sobrecargar alguno/s de
los operadores de comparación necesarios (<, <=, >, >=).

3. (1 punto) Implementa el siguiente programa en un fichero “principal.py” para probar la
funcionalidad:
• Declara una variable que referencie a un Alumno con DNI “34678904” y nombre “Pepe”.
• Declara una variable que referencie a un Alumno con DNI “17679456” y nombre “Andrea”
con saldo inicial de 125€.
• Declara una variable que referencie a un curso presencial de título “Diseño de Bases de
Datos” con fecha de inicio y fin 5/05/2019. El precio del curso es de 50€, la duración es de
un día de clase con 8 horas de clase y un cupo de 20 alumnos.
• Declara una variable que referencie a un curso online de título “Administración de Bases de
Datos” con fecha de inicio 12/05/2019 y fin 16/05/2019. El precio del curso es de 50€, la
duración es de 5 días y tiene como prerequisito que se haya realizado el curso presencial de
“Diseño de Bases de Datos”.
• Matricula a los dos alumnos en el curso presencial.
• Expide el título de todos los alumnos del curso presencial, mostrando el resultado por la
consola.
• Matricula al alumno Pepe en el curso online.
• Expide el título de todos los alumnos del curso online, mostrando el resultado por la
consola.

"""
from lib.Fachada import *

fachada = Fachada()
while True:
    print("\n*********************************")
    print("0. Salir **************************")
    print("1. Crear alumno *******************")
    print("2. Crear curso Presencial *********")
    print("3. Crear curso Online *************")
    print("4. Matricular alumno desde curso **")
    print("5. Matricular en curso desde alumno")
    print("6. Expedir certificado alumno *****")
    print("7. Mostrar alumnos ****************")
    print("8. Mostrar cursos *****************")
    print("9. Cargar alumnos de fichero ******")
    print("10. Cargar cursos presenciales ****")
    print("11. Cargar cursos online **********")
    opcion = int(input("Introduce una opción: "))
    if opcion == 0: break;
    if opcion == 1:
        nombre = input("Dime un nombre: ")
        dni = input("Dime un DNI: ")
        saldo = int(input("Dime un saldo: "))
        alum = fachada.crearAlumno(nombre, dni, saldo)
        print(alum)

    if opcion == 2:
        codigo = input("Código: ")
        titulo = input("Título: ")
        fechainicio = input("Fecha inicio: ")
        fechafin = input("Fecha fin: ")
        dias = int(input("Dias: "))
        horas = int(input("Horas: "))
        precio = float(input("Precio: "))
        cupo = int(input("Cupo: "))
        curs = fachada.crearCursoPresencial(codigo, titulo, fechainicio, fechafin, dias, horas, precio, cupo)
        print(curs)

    if opcion == 3:
        codigo = input("Código: ")
        titulo = input("Título: ")
        fechainicio = input("Fecha inicio: ")
        fechafin = input("Fecha fin: ")
        dias = int(input("Dias: "))
        horas = int(input("Horas: "))
        precio = float(input("Precio: "))
        curs = fachada.crearCursoOnline(codigo, titulo, fechainicio, fechafin, dias, horas, precio)
        # Nos faltaría meter en la lista los cursos que son prerrequisitos de este usando su código.

    if opcion == 4:
        fachada.matricularAlumnoCurso()

    if opcion == 5:
        fachada.matricularCursoAlumno()

    if opcion == 6:
        fachada.expedirTitulo()

    if opcion == 7:
        print("\nDNI\t\t\tNombre\t\t\tSaldo\t\t\t")
        fachada.mostrarAlumnos()

    if opcion == 8:
        fachada.mostrarCursos()

    if opcion == 9:
        fachada.cargarDatosAlumnos("lib/alumno.txt")

    if opcion == 10:
        fachada.cargarDatosCursosPresenciales("lib/cursopresencial.txt")

    if opcion == 11:
        fachada.cargarDatosCursosOnline("lib/cursoonline.txt")

#alu = Alumno("Francisco Atoche",55555555)
#alu2 = Alumno("Pepito Pérez",55555551)
#print(alu)
#cur = Presencial("Prueba1", date(2015,12,1), date(2015,12,20), 10, 30, 20, 10)
#cur2 = Online("PruebaOnline", date(2015,12,1), date(2015,12,20), 10, 30, 20)
#cur2.listacursosprevios.append(cur)

#print(cur)
#alu.matricular(cur)
#alu2.matricular(cur)

#print(alu)

#print(cur.expedirTitulo(55555555))


#alu.matricular(cur2)
#print(alu)
#print("\n\nListado de alumnos matriculados de forma ordenada")
#cur.listadoAlumnosOrdenado()

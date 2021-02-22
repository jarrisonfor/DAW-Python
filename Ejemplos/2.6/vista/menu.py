from controlador.Controlador import *

control = Controlador()
control.cargarDatosAlumnos()
control.cargarDatosProfesores()
control.cargarDatosModulos()
opcion = -1
while opcion != 0:
    print("****************************+******")
    print("0. Salir **************************")
    print("1. Dar de alta alumno *************")
    print("2. Mostrar alumnos ****************")
    print("3. Dar de alta profesor ***********")
    print("4. Mostrar profesores *************")
    print("5. Dar de alta un módulo **********")
    print("6. Mostrar todos los módulos ******")
    print("7. Dar de alta una matrícula ******")
    print("***********************************")
    print("8. Asignar módulo a profesor ******")
    print("9. Añadir detalle de matrícula ****")
    print("10. Calificar módulos matrícula ***")
    print("*******************************+***")
    print("11. Borrar alumno *****************")
    print("12. Borrar profesor ***************")
    print("13. Borrar matrícula **************")
    print("14. Borrar módulo *****************")
    print("****************************+******")
    try:
        opcion = int(input("Escoja una opción: "))
    except:
        print("Ha introducido un valor erróneo")

    if opcion == 0:
        print("Adios")
    elif opcion == 1:
        control.listarAlumnos()
        dni = input ("Dime DNI:")
        if control.buscarAlumnoDNI(dni):
            print("El alumno ya existe con ese DNI")
        else:
            nexp = input ("Dime Expediente:")
            if control.buscarAlumnoEXP(nexp):
                print("El alumno ya existe con ese número de expediente")
            else:
                nombre = input("Nombre:")
                apellidos = input("Apellidos:")
                direccion = input("Dirección:")
                telefono = input("Teléfono:")
                fecha_n = input("Fecha nacimiento:")
                if control.CrearAlumno(dni, nombre, apellidos, direccion, telefono, nexp, fecha_n):
                    print("Se ha insertado el alumno correctamente")

    elif opcion == 2:
        control.mostrarAlumnos()

    elif opcion == 3:
        control.listarProfesores()
        dni = input("Dime DNI:")
        if control.buscarProfesorDNI(dni):
            print("El profesor ya existe con ese DNI")
        else:
            nombre = input("Nombre:")
            apellidos = input("Apellidos:")
            direccion = input("Dirección:")
            telefono = input("Teléfono:")
            vinculo = input("Vínculo:")
            especialidad = input("Especialidad:")
            control.CrearProfesor(dni, nombre, apellidos, direccion, telefono, vinculo, especialidad)

    elif opcion == 4:
        control.mostrarProfesores()

    elif opcion == 5:
        codigo = input("Código del módulo:")
        if control.buscarModulo(codigo):
            print("Ya existe un módulo con ese código")
        else:
            nombre = input("Nombre del módulo:")
            control.listarProfesores()
            dniprofesor = input("DNI del profesor:")
            control.CrearModulo(codigo, nombre, dniprofesor)

    elif opcion == 6:
        control.mostrarModulos()

    else:
        print("La opción introducida no existe")
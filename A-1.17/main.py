import os

numero1 = int(input('Introduzca número 1: '))
numero2 = int(input('Introduzca número 2: '))
while 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*********************')
    print('0.Salir ')
    print('*********************')
    print(f'1. Modificar número 1: {numero1}')
    print(f'2. Modificar número 2: {numero2}')
    print('*********************')
    print('3. Sumar')
    print('4. Restar')
    print('5.Multiplicar')
    print('6.Dividir')
    print('*********************')

    opcion = int(input('Escoja una opción: '))

    if opcion == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        exit(0)
    elif opcion == 1:
        numero1 = int(input('Introduzca número 1: '))
    elif opcion == 2:
        numero2 = int(input('Introduzca número 2: '))
    elif opcion == 3:
        print(f'El resultado de la Suma es: {numero1 + numero2}')
    elif opcion == 4:
        print(f'El resultado de la Resta es: {numero1 - numero2}')
    elif opcion == 5:
        print(f'El resultado de la Multiplicacion es: {numero1 * numero2}')
    elif opcion == 6:
        print(f'El resultado de la Division es: {numero1 / numero2}')
    else:
        print('No existe una opcion con ese valor')
    input("Presiona Enter para continuar")

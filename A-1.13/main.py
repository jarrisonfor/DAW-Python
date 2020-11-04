def fscanf(tipoMotor):
    if tipoMotor == 0:
        print('No hay establecido un valor definido para el tipo de bomba')
    elif tipoMotor == 1:
        print('La bomba es una bomba de agua')
    elif tipoMotor == 2:
        print('La bomba es una bomba de gasolina')
    elif tipoMotor == 3:
        print('La bomba es una bomba de hormigón')
    elif tipoMotor == 4:
        print('La bomba es una bomba de pasta alimenticia')
    else:
        print('No existe un valor válido para tipo de bomba')


tipoMotor = int(input('Indica un numero de bomba: '))

fscanf(tipoMotor)

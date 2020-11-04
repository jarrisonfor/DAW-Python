letras = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
          'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E')
dni = int(input('Nº de DNI: '))
if dni > 99999999 or dni < 0:
    print('Dni invalido')
else:
    print(f'{dni}{letras[dni % 23]}')

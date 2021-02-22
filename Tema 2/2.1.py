"""
UT2-AEA1 Punto y Segmento
1. Cree una clase llamada Punto que tendrá como atributos las coordenadas X e Y del punto en cuestión.

Los métodos serán:

IntroduceX. Introduce la coordenada X.
IntroduceY. Introduce la coordenada Y.
Muestra_puntoX. Imprimirá por pantalla el mensaje de texto: X, donde X es la coordenada del punto.
Muestra_puntoY. Imprimirá por pantalla el mensaje de texto: Y, donde Y es la coordenada del punto.
Ejecute un programa que cree dos puntos.

2. Cree una clase llamada "Línea" o "Segmento". Sus atributos serán dos objetos de la clase Punto. Como método tendrá longitud, que devolverá la distancia entre los dos puntos que componen el segmento. Ejecute un programa que cree un segmento, muestre la longitud de ese segmento y el punto más cercano al origen.

distancia = math.sqrt ((x-x0)**2 + (y-y0)**2)
"""

from controllers.Linea import Linea
from controllers.Punto import Punto

punto1 = Punto()
punto2 = Punto(6,8)

linea = Linea(punto1, punto2)
linea.cambiarPunto1(Punto(1,2))
print("El punto con distancia menor al origen es", linea.puntocercano())
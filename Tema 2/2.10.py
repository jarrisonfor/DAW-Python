"""

UT2-AE0 Bombilla
Modelar una casa con muchas bombillas, de forma que cada bombilla se puede encender o apagar individualmente.

Para ello hacer una clase Bombilla con una variable privada que indique si está encendida o apagada, así como un método que nos diga el estado de una bombilla concreta.

Además, queremos poner un interruptor general, de forma que, si saltan los fusibles, todas las bombillas quedan apagadas.

Cuando el fusible se repara, las bombillas vuelven a estar encendidas o apagadas, según estuvieran antes del percance.

Cada bombilla se enciende y se apaga individualmente, pero solo responde que está encendida si su interruptor particular está activado y además hay luz general.

Modifica la clase Bombilla para poder regular la intensidad de luz de las bombillas de la casa.

Se desea dotar a la clase de una interfaz que permita subir (up) o bajar (down) la intensidad de la luz y mostrar sí es alta, media o baja la intensidad.

Supondremos que al inicio de encender la intensidad de la luz es alta.

"""

from controllers.Casa import Casa
from controllers.Bombilla import Bombilla

casa = Casa(True)

for i in range(0,2):
    casa.addBombilla(Bombilla())

casa.addBombilla('Bombilla')
casa.switchBombilla(5)

casa.getBombillas()
casa.switchBombilla(0)
casa.getBombillas()
casa.bajaIntensidadBombilla(0)
casa.getBombillas()
casa.subirIntensidadBombilla(0)
casa.getBombillas()

casa.switchInterruptor()
casa.getBombillas()

casa.switchInterruptor()
casa.getBombillas()


print(casa)
from modelo.cliente import *
from modelo.mecanico import *
from datetime import date

c1 = Cliente("12345678", "Fernando", "González", "C/ Fajardo 1", "928121212")
print(c1)
m1 = Mecanico("12345679", "Antonio", "Castillo", date(2000,10,10), 1000)
print(m1)
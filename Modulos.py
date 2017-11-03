#Importando modulos
import math

print math.sqrt(16)

#Podemos especificar funciones del modulo a importar
from math import ceil, floor

print ceil(3.7)
print floor(3.7)

#Importar todas las funciones de un modulo
from math import *

#Acortando los nombres de un modulo
import math as m

print(math.sqrt(16) == m.sqrt(16))

from math import sqrt

print(math.sqrt == m.sqrt == sqrt)  # => True
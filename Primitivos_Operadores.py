from __future__ import division
# Numero
print(3)

# Matematicas
print(1 + 1)
print(8 - 1)
print(10 * 2)
print(35 / 5)

# Division con enteros
print(5 / 2)

# Division con flotantes
print(2.0)
print(11.0 / 4.0)

#Division de enteros truncada
print(5 // 3)
print(5.0 // 3.0)
print(-5 // 3)
print(-5.0 // 3.0)

#Importar modulo de division
print(11 / 4)  # => 2.75  ...normal division
print(11 // 4)  # => 2 ...floored division

#Residuo
print(7 % 3)

#Exponensia
print(2 ** 4)

#Parentesis
print((1 + 3) * 2)

#Boleano
print(True and False)
print(False or True)
print(0 and 2)
print(-5 or 0)
print(0 == False)
print(2 == True)
print(1 == True)
print(not True)
print(not False)

# Igualidad
print(1 == 1)
print(2 == 1)
print(1 != 1)
print(2 != 1)
print(1 < 10)
print(1 > 10)
print(2 <= 2)
print(2 >= 2)

#Comparasion
print(1 < 2 < 3)
print(2 < 3 < 2)

#Cadena
print("Esto es una cadena.")
print('Esto tambien es una cadena.')

# Agregando cadenas
print("Hola " + "mundo!")
print("Hello " "world!")

#Multiplicando
print("Hola" * 3)

#Primera letra
print("Cadena"[0])

#Tamano
print(len("Cadena"))

#Formato de cadenas
x = 'manzana'
y = 'limon'
z = "Los elementos de la canasta son %s y %s" % (x, y)
print(z)

# Otro metodo de formato de cadenas
print("{} es un {}".format("Esto", "marcador"))
print("{0} pueden tener {1}".format("Las cadenas", "formato"))
# Palabras clave
"{nombre} quiere comer {comida}".format(nombre="Bob", comida="lasagna")

# None es un objeto
print(None)

# Usando is para comparar objetos
print("etc" is None)
print(None is None)

print(bool(0))
print(bool(""))
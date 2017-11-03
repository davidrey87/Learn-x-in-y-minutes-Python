
#Hacemos una variable
some_var = 5

# Si some_var es mayor a 10
if some_var > 10:
    print "some_var es mayor a 10"
elif some_var < 10:
    print "some_var es menor a 10"
else:
    print "some_var es 10."


"""
Los ciclos for iteran sobre listas
"""
for animal in ["perro", "gato", "raton"]:
    print "{0} es un mamifero".format(animal)


"""
Obteniendo un rango de numeros para imprimir
"""
for i in range(4):
    print i


"""
Obteniendo desde un rango superior e inferior
"""
for i in range(4, 8):
    print i



"""
Obteniendo un rango mientras sea menor a un numero
"""
x = 0
while x < 4:
    print x
    x += 1
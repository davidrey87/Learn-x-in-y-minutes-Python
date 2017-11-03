# Print
print "Yo soy Python, gusto en conocerte."

# Obtener Datos
dato = int(raw_input("Pon algun dato: "))
dato2 = int(input("Pon algun dato: "))
print(dato+dato2)

#Variable
var = 5
print(var)

#Expresiones
print("yahoo!" if 3 > 2 else 2)

# Lista
li = []
# Lista inicializada con datos
other_li = [4, 5, 6]
print(other_li)
# Agregando lista a posicion
li.append(1)
li.append(2)
li.append(4)
li.append(3)
print(li)
# Quitando el ultimo elemento de la pila
li.pop()
print(li)
# Poniendolo de regreso
li.append(3)
print(li)

#Accesando a la posicion de una lista
print(li[0])
#Asignando valor a la posicion de una lista
li[0] = 42
print(li[0])
#Accediendo al ultimo elemento
print(li[-1])
#Accediendo por rangos
print(li[1:3])
print(li[2:])
print(li[:3])
print(li[::2])
print(li[::-1])

del li[2]
print(li)

print(li + other_li)

print(li.extend(other_li))
print(li.remove(2))
print(li.insert(1, 2))
print(li.index(2))
print(1 in li)
print(len(li))

# Las tuplas son como las listas pero inmutables
tup = (1, 2, 3)
print(tup[0])
print(len(tup))
print(tup + (4, 5, 6))
print(tup[:2])
print(2 in tup)

# Desempacar tuplas en variables
a, b, c = (1, 2, 3)
d, e, f = 4, 5, 6

#Las tuplas son creadas por defecto
g = 4, 5, 6
#Intercambiando valores
e, d = d, e

#Un diccionario prellenado
filled_dict = {"uno": 1, "dos": 2, "tres": 3}

print(filled_dict["uno"])

#Obteniendo las llaves
print(filled_dict.keys())
#Obteneindo los valores
print(filled_dict.values())
#Obteniendo los el elemento
print(filled_dict.items())

#Revisando si existe una llave
print("one" in filled_dict)
print(1 in filled_dict)

#Usando get para evitar errores
print(filled_dict.get("uno"))
print(filled_dict.get("cuatro"))
#Valor por defecto cuando es necesario
print(filled_dict.get("one", 4))
print(filled_dict.get("four", 4))

# Inicializar set con un manojo de valores
some_set = set([1, 2, 2, 3, 4])
print(some_set)
# No se garantoza el prden
another_set = set([4, 3, 2, 2, 1])
print(another_set)
# En python 2.7
filled_set = {1, 2, 2, 3, 4}
print(filled_set)
# Agregando mas items
filled_set.add(5)
print(filled_set)
#Haciendo intersecciones
other_set = {3, 4, 5, 6}
print(filled_set & other_set)

#Union
print(filled_set | other_set)

#Diferencia
print({1, 2, 3, 4} - {2, 3, 5})

# Diferencia simetrica
print({1, 2, 3, 4} ^ {2, 3, 5})

# Revisa si el conjunto de la izquierda es un super conjunto de la derecha
print({1, 2} >= {1, 2, 3})

# Revisa si existen en el conjunto
print(2 in filled_set)
print(10 in filled_set)
#Usamos def para crear una funcion
def add(x, y):
    print "X es {0} y Y es {1}".format(x, y)
    return x + y

print(add(5, 6))

#Poniendo argumentos clave
print(add(y=6, x=5))

#Interpetando una tupla con *
def varargs(*args):
    return args

print(varargs(1, 2, 3))

# Tupla que es interpretada con argumentos como palabras clave
def keyword_args(**kwargs):
    return kwargs

print(keyword_args(big="foot", loch="ness"))

#Haciendo ambas a la vez
def all_the_args(*args, **kwargs):
    print args
    print kwargs


args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}

print(all_the_args(*args))
print(all_the_args(**kwargs))
print(all_the_args(*args, **kwargs))


# Podemos pasar los argumentos a otras funciones
def pass_all_the_args(*args, **kwargs):
    all_the_args(*args, **kwargs)
    print varargs(*args)
    print keyword_args(**kwargs)

# Function Scope
x = 5

def set_x(num):
    # La variable local x no es la misma que la global
    x = num
    print x

def set_global_x(num):
    global x #Accedemos ahora a la variable global
    print x
    x = num
    print x


set_x(43)
set_global_x(6)


# Python tiene funciones de primera clase
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_10 = create_adder(10)
add_10(3)

#Tambien hay funciones anonimas
print((lambda x: x > 2)(3))
print((lambda x, y: x ** 2 + y ** 2)(2, 1))

# Hay paquete de funciones de orden superior
print(map(add_10, [1, 2, 3]))
print(map(max, [1, 2, 3], [4, 2, 1]))

print(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))

# Podemos usar compresion de listas
print([add_10(i) for i in [1, 2, 3]])
print([x for x in [3, 4, 5, 6, 7] if x > 5])

# Puedes construir comprension de set y dict
print({x for x in 'abcddeef' if x in 'abc'})
print({x: x ** 2 for x in range(5)})
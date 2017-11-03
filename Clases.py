class Human(object):
    #El atributo de la clase es compartido a todas las instancias de la misma
    species = "H. sapiens"

    #Inicializamos la instancia.
    def __init__(self, name):
        self.name = name
        self.age = 0

    #Un metodo de la instancia
    def say(self, msg):
        return "{0}: {1}".format(self.name, msg)

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def grunt():
        return "*grunt*"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age


#Inistanciando la clase
i = Human(name="Ian")
print i.say("hi")

j = Human("Joel")
print j.say("hello")

#Lamando al metodo
print(i.get_species())

# Cambiando el atributo compartido
Human.species = "H. neanderthalensis"
print(i.get_species())

#Llamando el metodo estatico
print(Human.grunt())

#Actualizando la propiedad
i.age = 42

# Obteniendo la propiedad
print(i.age)
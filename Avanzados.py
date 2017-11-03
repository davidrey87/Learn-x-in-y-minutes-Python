# Generador de valores
def double_numbers(iterable):
    double_arr = []
    for i in iterable:
        double_arr.append(i + i)
    return double_arr

for value in double_numbers(range(1000000)):
    print value
    if value > 5:
        break

def double_numbers_generator(iterable):
    for i in iterable:
        yield i + i

for value in double_numbers_generator(xrange(1000000)):
    print value
    if value > 5:
        break

values = (-x for x in [1, 2, 3, 4, 5])
for x in values:
    print(x)

values = (-x for x in [1, 2, 3, 4, 5])
gen_to_list = list(values)
print(gen_to_list)  # => [-1, -2, -3, -4, -5]

def add_apples(func):
    def get_fruits():
        fruits = func()
        fruits.append('Apple')
        return fruits
    return get_fruits

@add_apples
def get_fruits():
    return ['Banana', 'Mango', 'Orange']

print ', '.join(get_fruits())

from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please

print say()
print say(say_please=True)
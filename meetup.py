a = 10
while a > 0:
    if a % 2 == 0:
        print(a)
    a -= 1


x, y, z = 1, 2, 3
print(x, y, z)


def printer(x, y, z):
    print(x)
    print(y)
    print(z)

printer(1, 2, 3)


a = sum((2, 23, 475, 70))
print(a)
help(sum)


def add(a, b):
    '''Prints sum of two elements'''
    s = a + b
    return s

help(add)



one_plus_two = add(1, 2)
print(one_plus_two)


def adder(x):
    def addy(y):
        return x + y
    return addy

add2 = adder(2)
print(add2(10))



print('Привет')

def greet():
    print('Привет')















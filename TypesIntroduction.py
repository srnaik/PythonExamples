from http.client import NotConnected


from decimal import *

# Python 3 has two basic numeric types - Integer and Floating point
def print_num(num):
    print('x is {}'.format(num))
    print(type(num))

    num = num * 2.1
    print('x is {}'.format(num))
    print(type(num))

    # In Python 3, two integer division gives floating point numbers (Python 2 gives integer division)
    num = 7 / 3
    print('x is {}'.format(num))
    print(type(num))

    num = 7 // 3
    print('x is {}'.format(num))
    print(type(num))

    num = 7 % 3
    print('x is {}'.format(num))
    print(type(num))

    # sse Decimal class when working with decimal /floating point values for precision
    a = Decimal('.10')
    b = Decimal('.30')
    x = a + a + a - b
    print('x is {}'.format(x))
    print(type(x))

def print_str():
    # Strings are objects in Python, even the literal strings
    name = 'sachin'
    print('Name is {}'.format(name))
    name = 'sachin'.capitalize()
    print('Name with Capital Letter {}'.format(name))
    name = 'sachin'.upper()
    print('Name with Upper Case Letters {}'.format(name))
    # Positional Arguments with Right Adjust and Left Adjust
    name = 'Sachin {0:>1} {1:<1}'.format('R', 'Naik')
    print('Name with Capital Letter {}'.format(name))

    middle_name = 'R'
    last_name = 'Naik'
    # f string is available from python version 3.6 and later
    name = f'Sachin {middle_name} {last_name} - Formatting with f string'
    print(name)


# In Python 3.0 all types are classes including the built-in types
def print_types():
    x = None
    print('x is {}'.format(x))
    print(type(x))

    x = 10
    print('x is {}'.format(x))
    print(type(x))

    x = 'abc'
    print('x is {}'.format(x))
    print(type(x))

    x = 10.20
    print('x is {}'.format(x))
    print(type(x))

if __name__ == '__main__':
    print_num(7)
    print_str()
    print_types()
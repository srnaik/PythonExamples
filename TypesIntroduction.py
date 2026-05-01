from http.client import NotConnected
from decimal import *
from traceback import print_list

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

def print_list_items():

    x = [1,2,3,4,5]
    x[2] = 42 # List items are mutable

    for i in x:
        print('i is {}'.format(i))

    y = (2,4,8,10,12)
    for i in y:
        print ('i is {0:>1} '.format(i))

    z = range(10,100,5)
    # z[9] = 20 -> Range Object Doesn't support assignment
    for i in z:
        print ('i is {0:>1} '.format(i))

def print_dictionary():
    dictionary = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
    for k,v in dictionary.items():
        print('Key is {} and Value is {}'.format(k,v))

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

def print_type_and_id():
    tuple_one = (1,'two', 3.0,[4,'four'],5)
    tuple_two = (1,'two', 3.0,[4,'four'],5)
    print('tuple_one is {}'.format(tuple_one))
    print('tuple_two is {}'.format(tuple_two))
    print('tuple_one type is {}', type(tuple_one))
    print('tuple_two type is {}', type(tuple_two))
    print(id(tuple_one[2]))
    print(id(tuple_two[2]))

    if tuple_one[2] == tuple_two[2]:
        print('Equal')
    else:
        print('Not Equal')

    if isinstance(tuple_one, tuple):
        print('Tuple')

    if isinstance(tuple_one[3],list):
        print('List')


if __name__ == '__main__':
    print_num(7)
    print_str()
    print_types()
    print_list_items()
    print_dictionary()
    print_type_and_id()


def main():
    n = 10
    numarray = [100]
    print(f"Value of numarray from main is {numarray}, it's id is {id(numarray)}")
    x = kitten(n,numarray)
    print(f"Value of variable x is {x}, it's id is {id(x)}")
    # Argument values are passed by value
    print(f"Value of variable n is {n}, it's id is {id(n)}")
    # Object reference is snow changed since it's updated in kitten method
    print(f"Value of numarray now from main is {numarray}, it's id is {id(numarray)}")

    a = ('Sachin','Rahul','Sourav','Anil')
    # -> We can call touple with an '*' , it passes the reference to the same object
    print_list_items(*a)
    print_list_items()

    dictionary = dict(One ='One', Two ='Two', Three ='Three')
    print_dictionary(**dictionary)
    print_dictionary()

# Non-default arguments must always follow default arguments
def kitten(n, numarray,p = 20):
    n = 5
    # Objects are always passed byy reference
    numarray[0] = 200
    print(f"Value of numarray from kitten is {numarray}, it's id is {id(numarray)}")
    print(f"Value of variable n is {n}, it's id is {id(n)}")
    print(f'Printing p from kitten {p}')
    return 'kitten'

def print_list_items(*args):
    if len(args):
        for arg in args:
            print(arg)
    else:
        print('Empty list')

def print_dictionary(**kwargs):
    if len(kwargs):
        for  key, value in kwargs.items():
            print(f"Key is {key} : Value is {value}")

        # for key in kwargs:
        #   print(f"Key is {key} : Value is {kwargs[key]}")

        else:
            print('Empty dictionary')


if __name__ == '__main__': main()
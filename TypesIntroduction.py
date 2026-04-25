def print_num(num):
    print('x is {}'.format(num))
    print(type(num))

def print_str():
    name = 'sachin'
    print('Name is {}'.format(name))
    name = 'sachin'.capitalize()
    print('Name with Capital Letter {}'.format(name))
    name = 'sachin'.upper()
    print('Name with Capital Letter {}'.format(name))

if __name__ == '__main__':
    print_num(7)
    print_str()
class MyString(str):

    def __str__(self):
        return self[::-1]

    def print_string(self, string):
        print(self)
        print(self.upper())
        print(self.lower())
        print(self.capitalize())
        print(self.title())
        print(self.swapcase())
        print(self.casefold())
        # concatenation of literal strings
        title = 'Sachin ' 'Naik'
        print(title)
        print('Hello, World.{}'.format(42 * 7))
        s1 = title
        s2 = s1 + ' What\'s up?'

        if id(s1) != id(s2):
            print(f'Id\'s of {s1} and {s2} are different')
            print(f'Id of s1 is {id(s1)} and s2 is {id(s2)}')
        else:
            print(f'Id\'s of {s1} and {s2} are same')
            print(f'Id of s1 is {id(s1)} and s2 is {s2}')

    # strings are first class objects in python
    def print_formatted_string(self, string):
        print('The value passed is {}'.format(string))
        y = 72
        print('Values of x and y {} {}'.format(string, y))
        print('Values of x and y with positional args {0} {1}'.format(string, y))
        print('Values of x and y with named variables {xx} {bb}'.format(xx=string, bb=y))
        print('Values of x and y with formatting instructions {0:<5} {1:+05}'.format(string, y))
        z = string * y * 1000
        print('The result is {:,}'.format(z))
        print('Printing in European Format {:,}'.format(z).replace(',','.'))
        print('The result is {:,.3f}'.format(z))




s = MyString('Hello, World.')
print(s)
s.print_string('Hello, World')
s.print_formatted_string(42)
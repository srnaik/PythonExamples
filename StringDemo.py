
# strings are first class objects in python
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
        # concatination of literal strings
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
s = MyString('Hello, World.')
print(s)
s.print_string('Hello, World')
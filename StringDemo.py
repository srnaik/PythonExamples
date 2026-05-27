
# strings are first class objects in python

print('Hello, World.')
print('Hello, World.'.upper())
print('Hello, World.'.lower())
print('Hello, World.'.title())
print('Hello, World.'.swapcase())
print('Hello, World.{}'.format(42*7))

class MyString(str):

    def __str__(self):
        return self[::-1]

s = MyString('Hello, World.')
print(s)
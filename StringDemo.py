
class StringDemo:

    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'Value of n from repr function is {self._n}'

    def __str__(self):
        return f'Value of n from str function is {self._n}'

s = StringDemo(5)
print(s)
print(repr(s))
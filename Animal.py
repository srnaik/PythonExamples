
class Animal:

    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'Kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'Duck'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rwar'


    def type(self, t = None):
       if t: self._type = t
       return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    # Overriding __str__ method from object class
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def print_animal(obj):
        if not isinstance(obj,Animal):
            raise TypeError('print_animal(): requires an animal')
        print('The {} is named {} and says {}'.format(obj.type(),obj.name(),obj.sound()))

def main():
    first_animal = Animal(type='Kitten', name='fluffy',sound='rwar')
    second_animal = Animal(type='Duck',name='Donald',sound='Quack')
    print_animal(first_animal)
    print_animal(second_animal)
    print_animal(Animal(type='velociraptor',name='veronica',sound='hello'))
    print(first_animal) # overridden __str__ method is invoked here

if __name__ == '__main__': main()

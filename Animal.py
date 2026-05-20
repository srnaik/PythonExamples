
class Animal:

    def __init__(self, **kwargs):
        self._type = kwargs['type']
        self._name = kwargs['name']
        self._sound = kwargs['sound']


    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

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

if __name__ == '__main__': main()

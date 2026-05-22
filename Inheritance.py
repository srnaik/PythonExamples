from http.client import NotConnected
from unittest import expectedFailure

from Animal import Animal


class Animal:
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

    def type(self, type = None):
        if type: self._type = type
        try: return self._type
        except AttributeError : return None

    def name(self, name = None):
        if name: self._name = name
        try: return self._name
        except AttributeError : return None

    def sound(self, sound = None):
        if sound: self._sound = sound
        try: return self._sound
        except AttributeError : return None

    def __str__(self):
        return f'The {self.type()} is named {self.name()} and says {self.sound()}'

class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'Duck'
        if 'type' in kwargs:  del kwargs['type']
        super().__init__(**kwargs)

class Lion(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def hunts(self, type):
        print(f'The {self.name()} hunts {type}')

def main():
    duck = Duck(name = 'Donald', sound = 'Quack')
    lion = Lion(type = 'King', name = 'Lion', sound = 'Roar')
    print(duck)
    print(lion)
    lion.hunts('animals')

if __name__ == '__main__': main()

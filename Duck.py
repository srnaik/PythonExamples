
class Duck:
    sound = 'Quack Quack'
    movement = 'Walks like a Duck.'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

def main():
    duck = Duck()
    duck.quack()
    duck.move()

if __name__ == '__main__': main()

class TupleDemo:

    def print_tuples(self):
        x = (1,2,3,4,5)
        y = x
        print(x)
        print(y)

        y = len(x)
        print(x)
        print(y)

        y = reversed(x)
        print(x)
        print(y)

        y = sum(x)
        print(y)

        y = any(x)
        print(y)

        y = all(x)
        print(y)

        y = min(x)
        print(y)

        y = max(x)
        print(y)

        y = (6,7,8,9,10)
        z = zip(x,y)
        for a,b in z:
            print(f' {a} - {b}')

        y = ('cat', 'dog', 'rabbit', 'lion')
        for a,b in enumerate(y): print(f' {a}: {b}')


tp = TupleDemo()
tp.print_tuples()
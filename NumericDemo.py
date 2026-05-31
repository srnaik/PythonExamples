from idlelib import mainmenu


class NumericDemo:

    def print_num(self, val):

        num = int(val)
        print(f'{num} is of type: {type(num)}')
        print(f'{val} is of type: {type(val)}')

        float_num = float(val)
        print(f'{float_num} is of type: {type(float_num)}')

        result = divmod(47, num)
        print(f'{result} is of type: {type(result)}')

        comp = complex(num)
        print(f'{comp} is of type: {type(comp)}')
def main():
    demo = NumericDemo()
    demo.print_num('10')

if __name__ == '__main__': main()
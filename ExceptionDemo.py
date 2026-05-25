
import sys

def main():

    try:
        # x = int('foo')
        y = 5/0
    except ValueError:
        print('Caught Value Error')
    except ZeroDivisionError:
        print(f'Caught ZeroDivisionError: {sys.exc_info()[1]}')
    except:
        print('Unknown Error')
    else:
        print('No Errors!')
        print({y})

if __name__ == '__main__': main()
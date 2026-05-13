# Decorator is form a metaprogramming


def func(f):
    #print('This is func')
    def func2():
        print(f'This is before the function call {f}')
        f()
        print(f'This is after the function call {f}')
    return func2

@func
def second_func():
    print('This is the second function')

# x = func(second_func)
# x()
second_func()
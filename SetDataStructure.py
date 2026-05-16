

def main():
    a = set("Java")
    b = set("Lava")
    print_items(a & b)


def print_items(items):
    print('{',end='')
    for item in items: print(item, end = ' ', flush = True)
    print('}')

if __name__ == '__main__': main()
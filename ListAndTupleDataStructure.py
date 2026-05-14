
# List is an ordered collection, it's sequential and iterable
def main():
    game = ['Rock','Paper','Scissors', 'Lizard','Spock']
    print_list_items(game)


def print_list_items(items):
    for item in items:
        print(item)
    print(f'Printing first item via indexing : {items[0]}')

if __name__ == '__main__': main()
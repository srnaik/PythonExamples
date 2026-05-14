
# List is an ordered collection, it's sequential and iterable
# List is mutable
def main():
    game = ['Rock','Paper','Scissors', 'Lizard','Spock']
    print_list_items(game)
    modify_and_print_list_items(game)
    tuple_example()


def print_list_items(items):
    for item in items:
        print(item, end = ' ', flush = True)
    print(f'Printing first item via indexing : {items[0]}')
    print(f'Printing based on slice (beginning and end) : {items[0:3]}') # index 3 is non-inclusive
    print(f'Printing based on beginning, end and step : {items[0:5:2]}') # beginning:end:step
    i = items.index('Paper')
    print(f'indexing of Paper is : {i}')


def modify_and_print_list_items(items):
    items.insert(0,'Soccer')
    items.append('Cricket')

    for item in items:
        print(item, end = ' ', flush = True)
    print(f'\n')
    items.remove('Lizard')

    for item in items:
        print(item, end = ' ', flush = True)
    print(f'\n')

    item = items.pop() # Removes last item from the list
    # items.pop(2) # Removes 3rd item from the list (list items index starts from zero)
    print(f'Popped item is: {item}', end = ' ', flush = True)
    print(f'\n')

    del items[0] # Same as removing an item based on index like items.pop(2)

    for item in items:
        print(item, end = ' ', flush = True)
    print(f'\n')

    print(f'Length of items array is : {len(items)}')
    print(','.join(items)) # join the list using the join method on the string type - (',' is a string here)

def tuple_example():
    game = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')
    # game.append('Soccer') Tuple is immutable, hence this line will give run-time error
    for item in game:
        print(item, end = ' ', flush = True)

if __name__ == '__main__': main()
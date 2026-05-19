from math import pi


def main():
    sequence = range(11)
    list_sequence = [x * 2 for x in sequence]
    print_items(sequence)
    print_items(list_sequence)
    # extra if-clause in the below statement is only allowed after the for clause
    list_items_not_divisible_by_three = [ x for x in sequence if x % 3 != 0 ]
    print_items(list_items_not_divisible_by_three)

    list_of_tuples = [(x, x**2)for x in sequence]
    print_items(list_of_tuples)

    list_item_with_pi = [round(pi,x) for x in sequence]
    print_items(list_item_with_pi)

    dict_items = {x: x**2 for x in sequence}
    print(dict_items)

    set_items = {x for x in 'superduper' if x not in 'pd' }
    print_items(set_items)


def print_items(items):
    for x in items: print(x, end = ' ', flush = True)
    print('\n')

if __name__ == '__main__': main()
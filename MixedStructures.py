
def main():
    range_list = range(11)
    list = [1,'Two',3, {'4': 'four'},5]
    tuple = ('One','Two',None,'Four','Five')
    set_items = set("Sachin Sourav Rahul")
    dict_items = dict(one = range_list, two = tuple, four = set_items)
    mixed_items =  [list,range_list,set_items,dict_items,tuple]
    print(dict_items)
    print(mixed_items)


if __name__ == '__main__':
    main()
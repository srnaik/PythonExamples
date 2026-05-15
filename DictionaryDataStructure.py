def main():
    create_dictionary_with_braces()
    create_dictionary_with_constructors()

    sportIconsDict = {'Cricket': 'Sachin', 'Soccer': 'Messi', 'Basketball': 'Michael', 'Sprint': 'Usain'}
    key = 'Cricket'
    result = search_key(key, sportIconsDict)

    if result: print(f'Key {key} is present')
    else: print(f'Key {key}  is not present')

def create_dictionary_with_braces():
    print('This function creates a dictionary with braces.')
    sportIconsDict = {'Cricket' :'Sachin', 'Soccer':'Messi', 'Basketball':'Michael', 'Sprint':'Usain'}
    # for item in dictionary: print(f'Key/Value Pairs is {item} : {dictionary[item]}')
    for key, value in sportIconsDict.items(): print (f'Key/Value Pairs is {key} : {value}')


def create_dictionary_with_constructors():
    print('This function Dictionary with Constructors')
    sportIconsDict = dict(Cricket ='Sachin', Soccer ='Messi', Basketball ='Michael', Sprint ='Usain')
    for key, value in sportIconsDict.items(): print(f'Key/Value Pairs is {key} : {value}')


def search_key (key, dictionary):
    return key in dictionary

if __name__ == '__main__': main()




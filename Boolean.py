
a = True
b = False
x = ('bear', 'bunny','tree', 'sky','rain')
y = 'bear'


if a and b :
    print('Both a and b are true')
else:
    print('Either a or b or both a and b are false')

if a or b:
    print('Either a or b or both a and b are true')
else:
    print('Both a and b are true')

# Membership operator -> in and not in
if y in x:
    print('y is in x')
else:
    print('y is not in x')

# Identity Operator -> is and is not
if a is b:
    print('a is b')
else:
    print('a is not b')

if False:
    print('if True')
elif True:
    print('elif False')
else:
    print('None')



# Conditional statement inn Python uses if elif and else keywords
x = 5

if x == 1:
    print('x is 1')
elif x == 2:
    print('x is 2')
elif x == 3:
    print('x is 3')
elif x == 4:
    print('x is 4')
elif x == 5:
    print('x is 5')
else:
    print('No Condition Matched')


# -> Python includes conditional ternary operator starting from python version 2.5
hungry = True
status = 'Feed the bear now!' if hungry else 'Do not Feed the bear!'
print(status)
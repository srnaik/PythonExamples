
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']

for i in words:
    if i == 'three' or i == 'one' or i == 'seven' or i == 'five' : continue
    print(i)

secret = 'Swordfish'
pw = ''

authorize = False
count = 0
max_attempts = 5

while pw != secret:
    count+=1
    if count > max_attempts: break
    if count == 3: continue # continue will shortcut the loop
    pw = input(F" {count}: What's the secret word? ")
else:
    authorize = True

print("Secret Matched" if authorize else "Secret Not Matched")


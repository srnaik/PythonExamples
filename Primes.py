
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0 : return False

        return True

n = 5
result = isPrime(n)

if(result):
    print('{} is a prime number'.format(n))
else:
    print('{} is not a prime number'.format(n))

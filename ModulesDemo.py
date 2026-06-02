import sys
import os
import random
import datetime

def main():
    version = sys.version_info
    print('Python  Version {}.{}.{}'.format(*version))

    platform = sys.platform
    print(f'Platform is {platform}')

    osname = os.name
    print(f'OS is {osname}')

    envpath = os.environ['PATH']
    print(f'envpath is {envpath}')

    curdir = os.getcwd()
    print(f'current directory is {curdir}')

    # os random number generator
    num = os.urandom(25)
    print(f'num is {num}')

    random_digit = random.randint(1,1000)
    print(f'random digit is {random_digit}')

    now = datetime.datetime.now()
    print(f'Date now is {now}')
    print(f'Year is {now.year}')

if __name__ == '__main__': main()
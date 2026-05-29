

def main():
    readbinary = open('python.jpg', 'rb')
    writebinary = open('python-copy.jpg', 'wb')
    while True:
        bufffer = readbinary.read(10240)
        if bufffer:
            writebinary.write(bufffer)
            print('.',end='', flush=True)
        else: break
    writebinary.close()
    readbinary.close()
    print('\nDone')



if __name__ == '__main__': main()
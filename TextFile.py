
def main():
    inputfile = open('lines.txt','rt')
    outputfile = open('lines-copy.txt','wt')
    for line in inputfile:
        outputfile.write(line)
        # print(line.rstrip(),file = outputfile) -> Another way to write content to file
        print('.',end='',flush=True)
    outputfile.close()
    inputfile.close()
    print('\nDone')


if __name__ == '__main__': main()
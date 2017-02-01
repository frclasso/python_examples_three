#!/usr/bin/env python3

#read the lines from the file


def main():

    #fh = open('lines.txt')
    #for index, line in enumerate(fh.readlines()):
    #    print(index, line, end='')

    s = 'This is a string'
    for i, c in enumerate(s):
        #print (i, c)
        if c == 's':
            print('index {} is an s'.format(i))

if __name__ == "__main__": main()
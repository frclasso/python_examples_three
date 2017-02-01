#!/usr/bin/env python3


def main():
    buffersize = 50000
    infile = open('dragon-tatoo.jpg', 'rb') #segundo argumento define a ação, r = read, w = write, a = append
    outfile  = open('new.jpg', 'wb')
    buffer  = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print ('.', end='')
        buffer = infile.read(buffersize)
    print()
    print('Done!!')

if __name__=='__main__':main()
#!/usr/bin/env python3


def main():
    infile = open('lines.txt', 'r') #segundo argumento define a ação, r = read, w = write, a = append
    outfile  = open('new.txt', 'w')
    for line in infile:
        print (line, file = outfile, end=' ')

    print('Done!!')

if __name__=='__main__':main()
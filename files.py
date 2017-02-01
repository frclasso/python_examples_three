#!/usr/bin/env python3


def main():
    f = open('lines.txt', 'r') #segundo argumento define a ação, r = read, w = write, a = append
    for line in f.readlines():
        print (line, end=' ')



if __name__=='__main__':main()
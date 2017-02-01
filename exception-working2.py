#!/usr/bin/env python3

def main():

    try:
        for line in  readfile('lines.doc'): print(line.strip())
    except IOError as e:
        print ("Cannot read file:", e)
    except ValueError as e:
        print ('Bad filename', e)


def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('File name must end with .txt')


if __name__ == '__main__':main()
#!/usr/bin/env python3


def main():
    try:
        fh = open('lines.txt')
        for line in fh:
            print(line.strip())
    except IOError as e:
        print ("Could not open the file:", e)


if __name__ == "__main__":main()
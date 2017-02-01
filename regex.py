#!/usr/bin/env python3

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        match = re.search('(Ipsum)', line)
        if match:
            print (match.group())


if __name__ ==  "__main__":main()
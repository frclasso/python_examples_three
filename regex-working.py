#!/usr/bin/env python3

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        match = re.search('(################)', line)
        if match:
            print(line.replace(match.group(), 'Lorem'), end='')


if __name__ ==  "__main__":main()
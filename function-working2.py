#!/usr/bin/env python3


def main():
    testfunc(1,2,3,4,42, 43, 44)


def testfunc(this, that, other, *args):
    print(this,'/', that,'/', other)
    for n in args:
        print (n, end=' / ')


if __name__ == "__main__":main()

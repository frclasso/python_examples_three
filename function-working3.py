#!/usr/bin/env python3


def main():
    testfunc(5,6,7,8,9,10, one=1, two=2,four=42)


def testfunc(this, that, other, *args, **kwargs):
    for k in kwargs:
        print(k, '==>', kwargs[k])
    for n in args:
        print(n)
    print(this, that, other)

if __name__ == "__main__":main()

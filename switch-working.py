#!/usr/bin/env python3


def main():
    choices = dict(
        one = 'first',
        two = 'second',
        tree = 'third',
        four = 'fourth',
        five = 'fifth'
    )

    v = 'one'
    print(choices.get(v, 'other number or value')) # treatment exceptions

if __name__ ==  "__main__": main()
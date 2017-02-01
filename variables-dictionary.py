#!/usr/bin/env python3

def main():
    d = dict(
        one = 1, two =2, tree = 3, four =4, five = 'Five'
    )
    d['seven'] = 7
    for k in sorted(d.keys()):
        print(k, d[k])


if __name__ == "__main__": main()


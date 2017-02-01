#!/usr/bin/env python3

#simple Fibonacci series
#The sumof two elements defines the next set


def main():
    a, b = 0, 1
    while b < 50:
        print(b, end=' / ')
        a, b = b, a + b

    print("Done")

if __name__ == "__main__": main()
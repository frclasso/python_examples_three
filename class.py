#!/usr/bin/env python3


class Duck:

    def __init__(self, value):
        self._v = value

    def quack(self):
        print("Quaaaaaack", self._v)

    def walk(self):
        print("Walnking!!!", self._v)

    def color(self):
        print("Black and white",self._v)

    def size(self):
        print("Very big duck!", self._v)


def main():

    donald = Duck(42)
    donald.quack()
    donald.walk()
    donald.color()
    donald.size()

    print ()

    franck = Duck(142)
    franck.quack()
    franck.walk()
    franck.color()
    franck.size()


if __name__ ==  '__main__':main()


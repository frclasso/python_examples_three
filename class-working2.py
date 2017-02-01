#!/usr/bin/env python3

class Duck():
    def __init__(self, **kwargs):
        self.properties = kwargs


    def quack(self):
        print("Quaaaaaack",)

    def walk(self):
        super().walk()  ## HERDANDO ATRIBUTO DA CLASSE ACIMA/SUPERIOR -  SUPER CLASSE
        print("Walnking!!!")

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    @property
    def color(self):
        return self.properties.get('color', None)

    @color.setter
    def color(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del self.properties['color']


def main():

    donald = Duck()
    donald.color = 'White'
    print(donald.color)


if __name__ =='__main__': main()


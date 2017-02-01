#!/usr/bin/env python3


class Duck:

    def __init__(self, **kwargs):
        self.variables=kwargs

    def quack(self):
        print("Quaaaaaack",)

    def walk(self):
        print("Walnking!!!")

    def set_variables(self, k, v):
        self.variables[k] = v

    def get_variables(self, k):
        return self.variables.get(k, None) #None is the default value

    def size(self):
        print("Very big duck!")


def main():

    donald = Duck()
    donald.set_variables('color', 'blue') #setting a color value
    print (donald.get_variables('color'))


if __name__ =='__main__': main()


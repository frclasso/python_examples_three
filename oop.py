#!/usr/bin/env python3


class AnimalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']


class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaaak",
        feathers = "The Duck has gray and white feathers.",
        bark = "The Duck cannot bark.",
        fur = "The Duck has no fur."
    )


class Person(AnimalActions):
    strings = dict(
        quack = "The Person imitates a duck.",
        feathers = "The Person takes a feather from the ground  and shows it",
        bark = "The Person says woof!",
        fur = "The Person puts on a fur coat."


    )


class Dog(AnimalActions):
    strings = dict(
        quack = "The Dog cannot quack",
        feathers = "The Dog has no feathers",
        bark = "Arf!",
        fur = "The Dog has white fur black spots."
    )


def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())


def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())


def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print(" - In the forest: ")
    for o in (donald, john, fido):
        in_the_forest(o)

    print (" - In in_the_doghouse: ")
    for o in (donald, john, fido):
        in_the_doghouse(o)

if __name__ == '__main__': main()
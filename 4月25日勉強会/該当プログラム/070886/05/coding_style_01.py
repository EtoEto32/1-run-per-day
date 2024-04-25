import sys
import os

class MyClass():
    def __init__(self):
        self.prop = "my class"

    def method1(self, arg):
        print(f"{self.prop} {arg}")


def main():
    cls1 = MyClass()
    cls1.prop = "cls1"
    cls1.method1("was created")


if __name__ == "__main__":
    main()
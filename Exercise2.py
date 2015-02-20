# Exercise2.py
# Authors: Sam Coon and Tyler Kapusniak
# Date: 2/19/15

class Prism(object):
    def __init__(self, ID, length = 0, width = 0, height = 0, perimeter = 0, area = 0, volume = 0):
        self.__ID = ID
        self.__length = length
        self.__width = width
        self.__height = height
        self.__perimeter = perimeter
        self.__area = area
        self.__volume = volume
        

    def numbers(self):
        print("\nPrism:",self.__ID)
        self.__length = int(input("Enter the length of the the prism: "))
        self.__width = int(input("Enter the width of the prism: "))
        self.__height = int(input("Enter the height of the prism: "))
        self.__perimeter = (4 * self.__length) + (4 * self.__width) + (4 *self.__height)
        self.__area = (self.__width * self.__length) * 2 + (self.__height * self.__length) * 2 + (self.__height * self.__width) * 2
        self.__volume = self.__width * self.__height * self.__length

        while self.__length < 1 or self.__height < 1 or self.__width < 1:
            print("Sorry the numbers you enter can't be less than 1. Try again.")
            print("\nPrism:",self.__ID)
            self.__length = int(input("Enter the length of the the prism: "))
            self.__width = int(input("Enter the width of the prism: "))
            self.__height = int(input("Enter the height of the prism: "))
            self.__perimeter = (4 * self.__length) + (4 * self.__width) + (4 *self.__height)
            self.__area = (self.__width * self.__length) * 2 + (self.__height * self.__length) * 2 + (self.__height * self.__width) * 2
            self.__volume = self.__width * self.__height * self.__length

    def __str__(self):
        print("Prism ID:", self.__ID)
        print("Length:" , self.__length)
        print("Width:", self.__width)
        print("Height:", self.__height)
        print("Perimeter(Total edge length):", self.__perimeter)
        print("Area:", self.__area)
        print("Volume:", self.__volume, "\n")


def main():
    choice = ""
    shape1 = Prism(1)
    shape2 = Prism(2)
    shape3 = Prism(3)
    while choice != 0:
        print(
            """
    Welcome to Prism Program!

    Select one of the choices below...
    ------------------------------------
    0. Exit
    1. Enter demensions for rectangular Prism
    2. Display Prisms demensions
    ------------------------------------
   """
            )

        choice = int(input("Enter the number of what you want: "))

        if choice == 0:
            print("Goobye!")

        elif choice == 1:
            shape1.numbers()
            shape2.numbers()
            shape3.numbers()

        elif choice == 2:
            shape1.__str__()
            shape2.__str__()
            shape3.__str__()
main()

# Exercise1.py
# Authors: Sam Coon and Tyler Kapusniak
# Date: 2/18/15

class rectangle(object):
    def __init__(self, ID, length=0, width=0, perimiter = 0, area = 0):
        self.__ID = ID
        self.__length = length
        self.__width = width
        self.__perimiter = perimiter
        self.__area = area

    def numbers(self):
        print("\nRectangle:", self.__ID)
        self.__length = int(input("What do you want the length of to be? "))
        self.__width = int(input("What do you want the width of rectangle to be? "))
        self.__perimiter = (self.__length * 2) + (self.__width * 2)
        self.__area = self.__length * self.__width
    
        while self.__length <= 0 or self.__width <= 0:
            print("Can not go that low. Retry.")
            print("\nRectangle:", self.__ID)
            self.__length = int(input("What do you want the length to be? "))
            self.__width = int(input("What do you want the width to be? "))
            self.__perimiter = (self.__length * 2) + (self.__width * 2)
            self.__area = self.__length * self.__width

    def __str__(self):
        print("Rectangle:", self.__ID)
        print("Length:", self.__length)
        print("Width:", self.__width)
        print("Perimiter:" , self.__perimiter)
        print("Area:", self.__area, "\n")
        
def main():

    choice = ""
    rect1 = rectangle(1)
    rect2 = rectangle(2)
    rect3 = rectangle(3)

    while choice != 0:
        print(
            """
        Welcome to Rectangle program!

        Choose what you want to do...
        ---------------------------------------
        0. Exit
        1. Set value for rectangles
        2. View rectangles current values
        ---------------------------------------
        """
            )

        choice = int(input("Enter the number of what you want to do: "))

        if choice == 0:
            print("Goodbye!")
        
        elif choice == 1:
            rect1.numbers()
            rect2.numbers()
            rect3.numbers()

        elif choice == 2:
            rect1.__str__()
            rect2.__str__()
            rect3.__str__()
            
main()

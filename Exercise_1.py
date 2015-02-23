# usr/bin/python3
# Program Name: Challenge_1.py
# Author: Luke Gosnell
# Contributors: Tom Morissey
# Date: 2/18/2015

class Rectangle(object):
    def __init__(self, ID):
        self.ID = ID
        self.width = 1+ID
        self.length = 1+ID
        self.area = 1+ID
        self.perimeter = 1+ID

    def widthLength(self):
        print("Rectangle ID:",self.ID)
        self.length = int(input("Length: "))
        while self.length < 1:
            print("Length cannot be less than 1.")
            self.length = int(input("Length: "))
        self.width = int(input("Width: "))
        while self.width < 1:
            print("Width cannot be less than 1.")
            self.width = int(input("Width: "))
            
    def additionalAttributes(self):
        self.area = self.length * self.width
        self.perimeter = (2 * self.width) + (2 * self.length)
        
    def __str__(self):
        print("Rectangle ID: ", self.ID)
        print("Rectangle Length: ", self.length)
        print("Rectangle Width: ", self.width)
        print("Rectangle Perimeter: ", self.perimeter)
        print("Rectangle Area: ", self.area)
        
        
def main():
    userChoice = ""
    rectangle1 = Rectangle(1)
    rectangle2 = Rectangle(2)
    rectangle3 = Rectangle(3)
    choice = 0
    
    while choice != 1:
        print(
            """

        MENU
        ___________________________________
        1 - Exit
        2 - Set value for rectangles
        3 - View rectangles current values
        ___________________________________
        
        """
            )

        choice = int(input("Choice: "))

        if choice == 1:
            print("Exiting")
            input("Press enter to exit. ")
        
        elif choice == 2:
            rectangle1.widthLength()
            rectangle2.widthLength()
            rectangle3.widthLength()
            rectangle1.additionalAttributes()
            rectangle2.additionalAttributes()
            rectangle3.additionalAttributes()
            

        elif choice == 3:
            rectangle1.__str__()
            rectangle2.__str__()
            rectangle3.__str__()
            
main()
            

# usr/bin/python3
# Program Name: Exercise_2.py
# Author: Luke Gosnell
# Contributors: Tom Morissey
# Date: 2/19/2015

class Prism(object):
    def __init__(self, ID):
        self.ID = ID
        self.width = 1+ID
        self.length = 1+ID
        self.height = 1+ID
        self.volume = 1+ID
        self.perimeter = 1+ID
        self.surfaceArea = 1+ID

    def widthLengthHeight(self):
        print("Prism ID:",self.ID)
        self.length = int(input("Length: "))
        while self.length < 1:
            print("Length cannot be less than 1.")
            self.length = int(input("Length: "))
        self.width = int(input("Width: "))
        while self.width < 1:
            print("Width cannot be less than 1.")
            self.width = int(input("Width: "))
        self.height = int(input("Height: "))
        while self.height < 1:
            print("Height cannot be less than 1.")
            self.height = int(input("Height: "))
            
    def additionalAttributes(self):
        self.volume = self.length * self.width * self.height
        self.perimeter = 4 * (self.height + self.width + self.length) + (2 * self.width) + (2 * self.length)
        self.surfaceArea = (2 * self.length * self.width) + 2 * (self.length + self.width)
        
        
    def __str__(self):
        print("Prism ID: ", self.ID)
        print("Prism Length: ", self.length)
        print("Prism Width: ", self.width)
        print("Prism Perimeter: ", self.perimeter)
        print("Prism Surface Area: ", self.surfaceArea)
        print("Prism Height: ", self.height)
        
        
def main():
    userChoice = ""
    prism1 = Prism(1)
    prism2 = Prism(2)
    prism3 = Prism(3)
    choice = 0
    
    while choice != 1:
        print(
            """

        MENU
        ___________________________________
        1 - Exit
        2 - Set value for prisms
        3 - View prisms current values
        ___________________________________
        
        """
            )

        choice = int(input("Choice: "))

        if choice == 1:
            print("Exiting")
            input("Press enter to exit. ")
        
        elif choice == 2:
            prism1.widthLengthHeight()
            prism2.widthLengthHeight()
            prism3.widthLengthHeight()
            prism1.additionalAttributes()
            prism2.additionalAttributes()
            prism3.additionalAttributes()
            

        elif choice == 3:
            prism1.__str__()
            prism2.__str__()
            prism3.__str__()
            
main()
                   

#! usr/bin.python3
# Program Name: Challenge_1.py
# Author: Thomas Morrissey
# Date Written: 2-18-2015
# This program is based around the program made by Alton Stillwell
# Puesdocode:
#   The Goal of this challegne is to create three different rectangles then print the results.
#   I acomplished this by create 5 different functions, str, init, GetWidthAndLength, CreatePerimeter, and CreateArea. str prints the data created, init create each object as a part of the class,
#   GetLengthAndWidth gets the length and Width of each rectangle, CreatePerimeter create the attribute of perimeter for each rectangle, CreateArea creates the area attribute for each rectangle. 
class rectangle:# Creates the class
    def __init__(self, Id):# Initiazes each object into a rectangle.
        self.Id=Id
        self.length=1+Id
        self.width=1+Id
    def GetWidthAndLength(self):# Gets the width and length.
        self.width=self.length=0
        print("Please set the Length and Width Values for Rectangle", self.Id)
        print("Please set Width and Length to a value above 0.")
        print("Thank you!")
        while self.width < 1:
            self.width=int(input("Width Value: "))
            if self.width < 1:
                print("Please reset Width.")
        while self.length < 1:
            self.length=int(input("Length value: "))
            if self.length < 1:
                print("Please reset Length.")
    def CreatePerimeter(self):# Create a new attribute called perimeter.
        Perimeter=(self.length * 2) + (self.width * 2)
        self.perimeter=Perimeter
    def CreateArea(self):# Creates a attribute called Area.
        Area= self.width * self.length
        self.area = Area
    def __str__(self):# Sets up how the data organized when printed.
        print("Rectangle Id:", self.Id)
        print("Rectangle Length:", self.length)
        print("Rectangle Width:", self.width)
        print("Rectangle Perimeter:", self.perimeter)
        print("Rectangle Area:", self.area)
        return "- - - - - - - - - - - "
# Main Functions!
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def main():
    Rectangle0=rectangle(0)
    Rectangle1=rectangle(1)
    Rectangle2=rectangle(2)
    print("Welcome to Challenge_1!")
    print("This challenge requires the user to create three different rectangles and print out the results!")
    Rectangle0.GetWidthAndLength()
    Rectangle1.GetWidthAndLength()
    Rectangle2.GetWidthAndLength()
    Rectangle0.CreatePerimeter()
    Rectangle1.CreatePerimeter()
    Rectangle2.CreatePerimeter()
    Rectangle0.CreateArea()
    Rectangle1.CreateArea()
    Rectangle2.CreateArea()
    print("- - - - - - - - - - -")
    print(Rectangle0)
    print(Rectangle1)
    print(Rectangle2)
    input("Please press the <Enter> key to exit.")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
main()



































    
        
        
    

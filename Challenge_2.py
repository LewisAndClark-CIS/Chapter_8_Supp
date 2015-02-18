#! usr/bin/python3
# Program Name: Challenge_2.py
# Author: Thomas Morrissey
# Date Written: 2-18-2015
# Pusedocode:
#   This challenge is about creating three different prisms and adding attributes for each prism.
#   I accomplished this by creating my class, having 4 different methods for that class
#   (one to initize them, one to get the 3 main attributes, one to get the other 3, and the lst one to control how the data is organized when the program has the print the object),
#   and 1 main functioons to organize everything. 
class Prism:#My Class For the challenge.
    def __init__(self, Id):# This method initizes them.
        self.Id=Id
        self.Height=1+Id
        self.Length=1+Id
        self.Width=1+Id
    def GetLengthHeightWidth(self):#This method gets the first 3 sttributes.
        self.Height=self.Length=self.Width=0
        print("Please set the values of Height, Width, and Length for Prism", self.Id)
        print("No value can not be under 1.")
        while self.Height < 1:
            self.Height=int(input("Height: "))
            if self.Height < 1:
                print("Please reset Height.")
        while self.Length < 1:
            self.Length = int(input("Length: "))
            if self.Length < 1:
                print("Please reset Length.")
        while self.Width < 1:
            self.Width = int(input("Width: "))
            if self.Width < 1:
                print("Please reset Width.")
    def CreatingAdditionalAttributes(self):#This method gets the last 3 attributes.
        Perimeter = SurfaceArea = Volume = 0
        Perimeter = 4 * (self.Height + self.Width + self.Length)
        SurfaceArea = 2*(self.Length * self.Height) + 2*(self.Length * self.Width) + 2*(self.Width * self.Height)
        self.Volume = self.Height * self.Length * self.Width
        self.Perimeter=Perimeter
        self.SurfaceArea=SurfaceArea
    def __str__(self):# This controls how the data is organized. 
        print("Prism Id:", self.Id)
        print("Prism Height:", self.Height)
        print("Prism Length", self.Length)
        print("Prism Width:", self.Width)
        print("Prism Perimeter:", self.Perimeter)
        print("Prism Surface Area:", self.SurfaceArea)
        print("Prism Volume:", self.Volume)
        return "- - - - - - - - - - - - - - - - - - - -"
# Main Function!
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def main():
    Prism0=Prism(0)
    Prism1=Prism(1)
    Prism2=Prism(2)
    print("Welcome to Challenge_2.py!")
    print("The goal of this program is to create three different prisms with the following parimeters: width, length, height, volume, perimter, and surface area.")
    Prism0.GetLengthHeightWidth()
    Prism1.GetLengthHeightWidth()
    Prism2.GetLengthHeightWidth()
    Prism0.CreatingAdditionalAttributes()
    Prism1.CreatingAdditionalAttributes()
    Prism2.CreatingAdditionalAttributes()
    print("- - - - - - - - - - - - - - - - - - - -")
    print(Prism0)
    print(Prism1)
    print(Prism2)
    input("Please press <Enter> to Exit.")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
main()

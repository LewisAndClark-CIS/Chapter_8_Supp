################
# Exercise1 for Chapter 8
# Author: Alton Stillwell
# Date: 2/18/15
################
class Rectangle(object):
    def __init__(self, ID):
        self.length = 1 + ID
        self.width = 1 + ID
        self.ID = "ID" + str(ID)
        print("A new rectangle was created!")
        print(self.ID)
    def __str__(self):
        print("Rectangle ID:",self.ID)
        print("Rectangle Width:", self.width)
        print("Rectangle Length:",self.length)
        print("Rectangle Perimeter:",((self.length * 2) + (self.width * 2)))
        print("Rectangle Area:",(self.length * self.width))
        print("~~~~~~~~~~~~~~")
    def setWidth(self):
        print("Rectangle:", self.ID)
        self.width = int(input("Enter new width for rectangle: "))
        print(self.ID+"'s width is now set to", str(self.width) + "\n")
    def setLength(self):
        print("Rectangle", self.ID)
        self.length = int(input("Enter new lengthfor rectangle: "))
        print(self.ID+"'s length is now set to", str(self.length) + "\n")
# main
ID0 = Rectangle(0)
ID1 = Rectangle(1)
ID2 = Rectangle(2)
print("""
~~~~~~~~
0 - Quit
1 - Set Width
2 - Set Length
3 - Print All
~~~~~~~~
""")
choice = int(input("Choice: "))
print()
while choice != 0:
    if choice == 1:
        ID0.setWidth()
        ID1.setWidth()
        ID2.setWidth()
    elif choice == 2:
        ID0.setLength()
        ID1.setLength()
        ID2.setLength()
    elif choice == 3:
        ID0.__str__()
        ID1.__str__()
        ID2.__str__()
    else:
        print(choice,"is not a valid choice!")
    print("""
0 - Quit
1 - Set Width
2 - Set Length
3 - Print All
""")
    choice = int(input("Choice: "))
    print()

################
# Exercise2 for Chapter 8
# Author: Alton Stillwell
# Date: 2/18/15
################
class Prism(object):
    def __init__(self, ID):
        self.length = 1 + ID
        self.width = 1 + ID
        self.height = 1 + ID
        self.ID = "ID" + str(ID)
        print("A new prism was created!")
        print(self.ID)
    def __str__(self):
        print("Prism ID:",self.ID)
        print("Prism Width:", self.width)
        print("Prism Length:",self.length)
        print("Prism Height:",self.height)
        print("Prism Volume:", (self.width * self.length * self.height))
        print("~~~~~~~~~~~~~~")
    def setWidth(self):
        print("Prism:", self.ID)
        self.width = int(input("Enter new width for prism: "))
        print(self.ID+"'s width is now set to", str(self.width) + "\n")
    def setLength(self):
        print("Prism", self.ID)
        self.length = int(input("Enter new lengthfor prism: "))
        print(self.ID+"'s length is now set to", str(self.length) + "\n")
    def setHeight(self):
        print("Prism", self.ID)
        self.height = int(input("Enter new height for prism: "))
        print(self.ID+"'s height is now set to", str(self.height) + "\n")
# main
ID0 = Prism(0)
ID1 = Prism(1)
ID2 = Prism(2)
print("""
~~~~~~~~
0 - Quit
1 - Set Width
2 - Set Length
3 - Set Height
4 - Print All
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
        ID0.setHeight()
        ID1.setHeight()
        ID2.setHeight()
    elif choice == 4:
        ID0.__str__()
        ID1.__str__()
        ID2.__str__()
    else:
        print(choice,"is not a valid choice!")
    print("""
0 - Quit
1 - Set Width
2 - Set Length
3 - Set Height
4 - Print All
""")
    choice = int(input("Choice: "))
    print()

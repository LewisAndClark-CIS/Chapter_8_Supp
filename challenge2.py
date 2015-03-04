#Andrew Hecky
"""
2) Create a class called Prism, which does all the same things as rectangle, excpet that it
uses a third attribute: Height. Also, it should have sets and gets for height, and include
a new method: volume, which returns the volume of the prism.
"""

prisms =[]

class Prism(object):

    def __init__(self, l, w, h, ID):
        self.l = l
        self.w = w
        self.h = h
        self.ID = ID
        
    def __str__(self):
        the_string = "\tLength: " + str(self.l) + "\n"
        the_string += "\tWidth: " + str(self.w) + "\n"
        the_string += "\tHeight: " + str(self.h) + "\n"
        the_string += "\tSurface Area: " + str(2 * (self.l *self.w) + ((2*self.l + 2*self.w) * self.h)) + "\n"
#        the_string += "\tPerimeter: " + str((2 *(2*self.l + 2*self.w)) + (4 * self.h)) + "\n" ////////////////3D objects dont have perimeter
        the_string += "\tVolume: " + str(self.l * self.w * self.h) 
        print()
        
        return the_string

print("\nEnter information for Prism 1")
l = int(input("Length: "))
w = int(input("Width: "))
h = int(input("Height: "))
ID = 1
pri1 = Prism(l, w, h, ID)
prisms.append(pri1)


print("\nEnter information for Rectangle 2")
l = int(input("Length: "))
w = int(input("Width: "))
h = int(input("Height: "))
ID = 2
pri2 = Prism(l, w, h, ID)
prisms.append(pri2)

print("\nEnter information for Rectangle 3")
l = int(input("Length: "))
w = int(input("Width: "))
h = int(input("Height: "))
ID = 3
pri3 = Prism(l, w, h, ID)
prisms.append(pri3)

print("\nPrism 1: \n" + str(prisms[0]))
print("Prism 2: \n" + str(prisms[1]))
print("Prism 3: \n" + str(prisms[2]))


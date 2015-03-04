#Andrew Hecky
"""
1) Create a class called rectangle. The attributes for rectangle are:ID - based off of a
class attribute (page 222) Length - cannot be less than one Width - cannot be less than one
"""

rectangles =[]

class rectangle(object):

    def __init__(self, l, w, ID):
        self.l = l
        self.w = w
        self.ID = ID
        
    def __str__(self):
        the_string = "\tArea: " + str(self.l * self.w) + "\n"
        the_string += "\tPerimeter: " + str(2 * (self.l + self.w))
        print()
        
        return the_string

print("\nEnter information for Rectangle 1")
l = int(input("length: "))
w = int(input("Width: "))
ID = 1
rec1 = rectangle(l, w, ID)
rectangles.append(rec1)


print("\nEnter information for Rectangle 2")
l = int(input("length: "))
w = int(input("Width: "))
ID = 2
rec2 = rectangle(l, w, ID)
rectangles.append(rec2)

print("\nEnter information for Rectangle 3")
l = int(input("length: "))
w = int(input("Width: "))
ID = 3
rec3 = rectangle(l, w, ID)
rectangles.append(rec3)

print("\nRectangle 1: \n" + str(rectangles[0]))
print("Rectangle 2: \n" + str(rectangles[1]))
print("Rectangle 3: \n" + str(rectangles[2]))

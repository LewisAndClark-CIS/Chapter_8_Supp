# Exercise 1
# Author: Bo Meers
# Date: 25/2/15


boxes =[]

class rectangle(object):

    def __init__(self, l, w, h, ID):
        self.l = l
        self.w = w
        self.h = h
        self.ID = ID
        
    def __str__(self):
        the_string = "\tID: " + str(self.ID) + "\n"
        the_string += "\n\tLength: " + str(self.l)
        the_string += "\tWidth: " + str(self.w)
        the_string += "\tHeight: " + str(self.h) + "\n"
        the_string += "\tArea: " + str(self.l * self.w * self.h) + "\n"
        the_string += "\tPerimeter: " + str(2 * (self.l + self.w)) + "\n"
        return the_string
        #print(self.h)

print("\n\tEnter the values for the first rectangle\n")
l = int(input("length: "))
w = int(input("Width: "))
h = int(input("Height: "))
ID = 1
rec1 = rectangle(l, w, h, ID)
boxes.append(rec1)


print("\n\tEnter the values for the second rectangle\n")
l = int(input("length: "))
w = int(input("Width: "))
h = int(input("Height: "))
ID += 1
rec2 = rectangle(l, w, h, ID)
boxes.append(rec2)

print("\n\tEnter the values for the third rectangle\n")
l = int(input("length: "))
w = int(input("Width: "))
h = int(input("Height: "))
ID += 1
rec3 = rectangle(l, w, h, ID)
boxes.append(rec3)


#print("\n\tRectangle 1: " + boxes[0]))
print(boxes[0])
#print("\tRectangle 2: " + str(boxes))
print(boxes[1])
#print("\tRectangle 3: " + str(boxes))
print(boxes[2])

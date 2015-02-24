class Rectangle(object):
    def __init__(self, width, length, height):
        self.w = width
        self.l = length
        self.h = height
    def width(self):
        self.w = input("Please Insert the shape's width here: ")
    def length(self):
        self.l = input("Please Insert the shape's length here: ")
    def height(self):
        self.h = input("Please Insert the shape's height here: ")

    def perimeter(self):
        return (2 * self.w) + (2 * self.l)
    def area(self):
        return self.w * self.l
    def volume(self):
        return self.w * self.l * self.h

print("Length:", length, "Width:", width, "Height:", height, "Perimeter:", perimeter, "Area:", area, "Volume:", volume)

        

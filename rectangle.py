class Rectangle(object):
    def __init__(self, width, length):
        self.w = width
        self.l = length
    def width(self):
        self.w = input("Please Insert the shape's width here: ")
    def length(self):
        self.l = input("Please Insert the shape's length here: ")

    def perimeter(self):
        return (2 * self.w) + (2 * self.l)
    def area(self):
        return self.w * self.l

print("Length:", length, "Width:", width, "Perimeter:", perimeter, "Area:", area)

        

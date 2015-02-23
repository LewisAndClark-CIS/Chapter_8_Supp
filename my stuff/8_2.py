class Prism(object):
    def __init__(self, ID, length, width, height, volume):
        self.ID = ID
        self.length = length
        self.width = width
        self.perimeter = (2 * length) + (2 * width)
        self.area = (length * width)
        self.height = height
        self.volume = volume

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def set_length(self, set_to):
        self.length = set_to

    def set_width(self, set_to):
        self.width = set_to

    def getPerimeter(self):
        return self.perimeter

    def getArea(self):
        return self.area

    def getHeight(self):
        return self.height

    def set_height(self, set_to):
        self.height = set_to

    def getVolume(self):
        return self.volume

class Rectangle(object):
    def __init__(self, ID, length, width):
        self.ID = ID
        self.length = length
        self.width = width
        self.perimeter = (2 * length) + (2 * width)
        self.area = (length * width) 

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def set_length(self, set_to):
        self.length = set_to

    def set_width(self, set_to):
        self.width = set_to

    def getPerimeter(self):
        return self.perimeter

    def getArea(self):
        return self.area 
 
def main():
    print("""
    Welcome! Please make a square!

    Quit: 0
    Length: 1
    Width: 2
    Prism: 3
    
    """)
    ID = int(input("ID: "))
    width = int(input("Width: "))
    length = int(input("Length: "))


    rec = Rectangle(ID, length, width)

    prism = Prism(ID, length, width, height, volume)

    response = int(input("What would you like to do? "))
    if response == 0:
        print("Thank you for playing")
        print("Please press enter")
    elif response == 1:
        rec.set_length(int(input("Length: ")))
        print(rec.getLength(), "is the length you enterted")
        print(rec.getPerimeter())
        print(rec.getArea())
    elif response == 2:
        rec.set_width(int(input("Width: ")))
        print(rec.getWidth())
        print(rec.getPerimeter())
        print(rec.getArea())
    elif response == 3:
        prism.set_height(int(input("Height: ")))
        print(prism.getWidth())
        print(prism.getPerimeter())
        print(prism.getArea())
        print(prism.getHeight())
        print(prism.getVolume())
main()

#Tom helped with the program
class rectangle:
    def __init__ (self, Id):
        self.Length = 1 + Id
        self.width = 1 + Id
        self.Id = Id
    def measurement(self):
        self.Length =int(input("What is length of rectangle" + str(self.Id)+":"))
        self.width =int(input("What is width of rectangle" + str(self.Id)+":"))
        self.Perimeter = 2* self.Length + 2* self.width
        self.area = self.Length* self.width
        
    def __str__(self):
        print("Rectangle Id:", self.Id)
        print("Length:", self.Length)
        print("Width:", self.width)
        print("Perimeter:", self.Perimeter)
        print("Area:", self.area)
        return "- - - - - - "

def main():
    rectangle0 = rectangle(0)
    rectangle1 = rectangle(1)
    rectangle2 = rectangle(2)
    rectangle0.measurement()
    rectangle1.measurement()
    rectangle2.measurement()
    print("- - - - - - ")
    print(rectangle0)
    print(rectangle1)
    print(rectangle2)

main()

input("Please press <Enter> to exit.")

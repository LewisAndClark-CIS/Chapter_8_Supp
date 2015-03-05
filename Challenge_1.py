#Tom helped me and jose with makeing the whole thing so that the class can be cought up
#3-5-15
class rectangle:
    def __init__(self, Id):
        self.Length=1 + Id
        self.Width=1 + Id
        self.Id=Id
    def measurment(self):
        self.Length=int(input("What is the length of the rectangle "+str(self.Id)+":"))
        self.Width=int(input("What is the width of the rectangle "+ str(self.Id)+":"))
        self.Perimeter=2*self.Length + 2*self.Width
        self.Area=self.Length *self.Width
    def __str__(self):
        print("Rectangle Id:", self.Id)
        print("Rectangle Length:", self.Length)
        print("Rectangle Widgth:", self.Width)
        print("Rectangle Area:", self.Area)
        print("Rectangle preimeter:", self.Perimeter)
        return "- - - - - - -"

def main():
    rectangle0=rectangle(0)
    rectangle1=rectangle(1)
    rectangle2=rectangle(2)
    rectangle0.measurment()
    rectangle1.measurment()
    rectangle2.measurment()
    print("- - - - - - -")
    print(rectangle0)
    print(rectangle1)
    print(rectangle2)

main()

input("please press enter to exit")

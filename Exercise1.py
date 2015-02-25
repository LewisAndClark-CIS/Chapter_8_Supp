#Exercise1.py
#Karlos Calvillo
#In collaboration with Thomas Morrisey and Karl Pearson
#2/18/2015

class Rectangle:
    def __init__(self,Id):
        self.Id=Id
        self.width=1+Id
        self.length=1+Id
    def getWidthAndLength(self):
        self.width=self.length=0
        print('Set Length and Width values for',self.Id,'to a value >0')
        while self.width <1:
            self.width=int(input("Width Value: "))
            if self.width<1:
                print('Not valid, please try again')
        while self.length<1:
            self.length=int(input("Length Value: "))
            if self.length<1:
                print('Not valid, please try again')
    def PerimeterDef(self):
        Perimeter=(self.length*2)+(self.width*2)
        self.perimeter=str(Perimeter)
    def AreaDef(self):
        Area=self.length*self.width
        self.area=str(Area)
    def __str__(self):
        print("Rectangle ID:",self.Id)
        print("Rectangle Width=",self.width)
        print("Rectangle Length=",self.length)
        print("Rectangle Perimeter=",self.perimeter)
        print("Rectangle Area=",self.area)
        print("****************************")
def main():
    Rectangle0=Rectangle(0)
    Rectangle1=Rectangle(1)
    Rectangle2=Rectangle(2)
    print("Please create 3 rectangles!")
    Rectangle0.getWidthAndLength()
    Rectangle1.getWidthAndLength()
    Rectangle2.getWidthAndLength()
    Rectangle0.PerimeterDef()
    Rectangle1.PerimeterDef()
    Rectangle2.PerimeterDef()
    Rectangle0.AreaDef()
    Rectangle1.AreaDef()
    Rectangle2.AreaDef()
    print(Rectangle0)
    print(Rectangle1)
    print(Rectangle2)
    input("\n\nPress <Enter> to exit.")
main()

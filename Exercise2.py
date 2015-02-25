#Exercise2.py
#Karl Pearson
#In collaberation with Thomas Morrisey
#2/24/2015

class Prism:
    def __init__(self,Id):
        self.Id=Id
        self.width=1+Id
        self.length=1+Id
        self.height=1+Id
    def getMeasurements(self):
        self.width=self.length=self.height=0
        print('Set the length, width, and height values for',self.Id,'to a value >0')
        while self.width<1:
            self.width=int(input("Width Value: "))
            if self.width<1:
                print('Not valid, please try again')
        while self.length<1:
            self.length=int(input("Length Value: "))
            if self.length<1:
                print('Not valid, please try again')
        while self.height<1:
            self.height=int(input('Height Value: '))
            if self.height<1:
                print('Not valid, please try again')
    def PerimeterDef(self):
        Perimeter=(self.length*2)+(self.width*2)
        self.perimeter=str(Perimeter)
    def AreaDef(self):
        Area=self.length*self.width
        self.area=str(Area)
    def VolumeDef(self):
        Volume=self.length*self.width*self.height
        self.volume=str(Volume)
    def __str__(self):
        print("Prism ID:",self.Id)
        print("Prism Width=",self.width)
        print("Prism Length=",self.length)
        print("Prism Height=",self.height)
        print("Prism Perimeter=",self.perimeter)
        print("Prism Area=",self.area)
        print("Prism Volume=",self.volume)
        print("*****************************")
def main():
    Prism0=Prism(0)
    Prism1=Prism(1)
    Prism2=Prism(2)
    print('Please create 3 prisms!')
    Prism0.getMeasurements()
    Prism1.getMeasurements()
    Prism2.getMeasurements()
    Prism0.PerimeterDef()
    Prism1.PerimeterDef()
    Prism2.PerimeterDef()
    Prism0.AreaDef()
    Prism1.AreaDef()
    Prism2.AreaDef() 
    Prism0.VolumeDef()
    Prism1.VolumeDef()
    Prism2.VolumeDef()
    print(Prism0)
    print(Prism1)
    print(Prism2)
    input("\n\nPress <Enter> to exit.")
main()

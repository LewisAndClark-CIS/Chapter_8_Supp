class prism(object):
    def __init__(self, Id):
        self.Id = Id
        self.Height = 1 + Id
        self.Length = 1 + Id
        self.Width = 1 + Id
    def GetMeasurement(self):
        self.Height = int(input("Please enter the height of Prism"+str(self.Id)+":"))
        self.Width = int(input("Please enter the width of Prism"+str(self.Id)+":"))
        self.Length = int(input("Please enter the length of Prism"+str(self.Id)+":"))
        self.SurfaceArea = 2*(self.Length * self.Height) + 2*(self.Length * self.Width) + 2*(self.Width * self.Height)
        self.Perimeter = 4 * (self.Height + self.Width + self.Length)
        self.Volume = self.Height * self.Length * self.Width
    def __str__(self):
        print("Prism Id:",self.Id)
        print("Prism Height:", self.Height)
        print("Prism Length", self.Length)
        print("Prism Width:", self.Width)
        print("Prism Perimeter:", self.Perimeter)
        print("Prism Surface Area:", self.SurfaceArea)
        print("Prism Volume:", self.Volume)
        return "- - - - - - - - - - - - - - - - - - - -"
Prism0=prism(0)
Prism1=prism(1)
Prism2=prism(2)
Prism0.GetMeasurement()
Prism1.GetMeasurement()
Prism2.GetMeasurement()
print("- - - - - - - - - - - - - - - - - - - -")
print(Prism0)
print(Prism1)
print(Prism2)
input("Please press <Enter> to Exit.")


#code origin Tom  author me 
#tom helped me understand the code and how it works
#3-4-15

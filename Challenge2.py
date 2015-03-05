#Challenge2.py

class prism(object):

    def __init__(self, Id):
        self.Id=Id
        self.Height=1+Id
        self.Length = 1 + Id
        self.Width =1+ Id

    def GetMeasurment(self):
        self.Height = int(input("Enter Height of rectangle" + str(self.Id) + ": "))
        self.Width = int(input("Enter Width of rectangle" + str(self.Id) + ": "))
        self.Length + int(input("Enter Length of rectangle" + str(self.Id) + ": "))
        self.SurfaceArea = 2* (self.Length + self.Height) + 2* (self.Length + self.Width) + 2* (self.Width + self.Height)
        self.Perimeter = 4* (self.Length + self.Width + self.Height)
        self.Volume = self.Height* self.Length* self.Width

    def __str__(self):
        print("Prism Id:", self.Id)
        print("Prism Height:", self.Height)
        print("Prism Width:", self.Width)
        print("Prism Length:", self.Length)
        print("Prism Surface Area:", self.SurfaceArea)
        print("Prism Perimeter:", self.Perimeter)
        print("Prism Volume:", self.Volume)
        return "- - - - - - - - - - - - - - - - - -"

Prism0 = prism(0)
Prism1 = prism(1)
Prism2 = prism(2)
Prism0.GetMeasurment()
Prism1.GetMeasurment()
Prism2.GetMeasurment()

print("- - - - - - - - - - - - - - - - - -")
print(Prism0)
print(Prism1)
print(Prism2)

input("Press <Enter> to Exit.")

#Author: Jose Chica
#03/05/15
#With the help of Tom and Tyler
        
        

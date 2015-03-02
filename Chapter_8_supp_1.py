#Chapter_8_supp_1.py
#Joe Carty(With help from Tom Morrissey)
#2/19/15

class rectangle:
    def __init__(self,ID):
        self.id = ID
        self.width = 1+ID
        self.length = 1+ID
    def __str__(self):
        print("Rectangle ID: ",self.id)
        print("Length: ",self.length)
        print("Width: ",self.width)
        print("Perimeter: ",self.perimeter)
        print("Area: ",self.area)
        return "- - - - - - "
    
    def get_width_length(self):
        self.width=self.length=0
        print("Please define width and length values.")
        print("These values cannot be below one.")
        while self.width < 1:
            self.width=int(input("Width value: "))
            if self.width < 1:
                print("Please reset width value above 0.")
        while self.length < 1:
            self.length=int(input("Length value: "))
            if self.length < 1:
                print("Please reset length value above 0.")
                

    def additional_attributes(self):
        self.area=self.length*self.width
        self.perimeter= (2*self.length)+(self.width)

def main():
    rectangle0=rectangle(0)
    rectangle1=rectangle(1)
    rectangle2=rectangle(2)

    print("WELCOME TO MY PROGRAM!!!!")
    
    print("In this program I will create three different rectangles with the attributes: \nLength, Width, Area, and Perimeter.")

    rectangle0.get_width_length()
    rectangle1.get_width_length()
    rectangle2.get_width_length()

    rectangle0.additional_attributes()
    rectangle1.additional_attributes()
    rectangle2.additional_attributes()

    print(rectangle0)
    print(rectangle1)
    print(rectangle2)

main()
    

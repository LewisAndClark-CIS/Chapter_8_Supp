
class Rectangle(object):

    def __init__(self, length, width, boxid):
        self.length = length
        self.width = width
        self.boxid = boxid

    def __str__(self):
        info = "Rectangle Number: {}".format(self.boxid) + "\n"
        info += "Length: {}".format(self.length) + "\n"
        info += "Width: {}".format(self.width) + "\n"
        info += "Permimeter: {}".format((self.width * 2) + (self.length * 2)) + "\n"
        info += "Area: {}".format((self.width) * (self.length))
        info += "\n"
        return info


def main():
    menu = """Rectangle Creator
        0 - Quit
        1 - New Rectangle
        2 - View a Rectangle
        3 - View all Rectangles
            """
    print(menu)
    choice = None
    choice = input("Choice: ")

    rectangles = []

    while choice != "0":

        numOfRec = 1
        if choice == "1":
            length = int(input("Length: "))
            width = int(input("Width: "))
            boxid = numOfRec

            if numOfRec == 1:
                rec1 = Rectangle(length, width, boxid)
                rectangles.append(rec1)
            elif numOfRec == 2:
                rec2 = Rectangle(length, width, boxid)
                rectangles.append(rec2)
            elif numOfRec == 3:
                rec3 = Rectangle(length, width, boxid)
                rectangles.append(rec3)
            elif numOfRec == 4:
                rec4 = Rectangle(length, width, boxid)
                rectangles.append(rec4)
            elif numOfRec == 5:
                rec5 = Rectangle(length, width, boxid)
                rectangles.append(rec5)
            elif numOfRec == 6:
                rec6 = Rectangle(length, width, boxid)
                rectangles.append(rec6)
            elif numOfRec == 7:
                rec7 = Rectangle(length, width, boxid)
                rectangles.append(rec7)

            numOfRec += 1
            print(menu)
            choice = input("Choice: ")


        if choice == "2":
            found = False
            while found == False:
                try:
                    recToPrint = int(input("Which one(0-6): "))
                    print(rectangles[recToPrint])
                    found = True
                except (IndexError, ValueError):
                    print("Rectangle not found")


            print(menu)
            choice = input("Choice: ")

        if choice == "3":
            for i in rectangles:
                print(i)

        print(menu)
        choice = input("Choice: ")



main()
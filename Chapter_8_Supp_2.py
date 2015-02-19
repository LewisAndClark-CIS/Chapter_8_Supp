class Prism(object):

    def __init__(self, length, width, height ,boxid):
        self.length = length
        self.width = width
        self.height = height
        self.boxid = boxid

    def __str__(self):
        info = "Prism Number: {}".format(self.boxid) + "\n"
        info += "Length: {}".format(self.length) + "\n"
        info += "Width: {}".format(self.width) + "\n"
        info += "Height: {}".format(self.width) + "\n"
        info += "Volume: {}".format((self.width * self.length) * self.height)
        info += "\n"
        return info


def main():
    menu = """Prism Creator
        0 - Quit
        1 - New Prism
        2 - View a Prism
        3 - View all Prisms
            """
    print(menu)
    choice = None
    choice = input("Choice: ")
    prisms = []

    while choice != "0":
        numOfRec = 1
        if choice == "1":
            length = int(input("Length: "))
            width = int(input("Width: "))
            height = int(input("Height: "))
            boxid = numOfRec

            if numOfRec == 1:
                rec1 = Prism(length, width, height, boxid)
                prisms.append(rec1)
            elif numOfRec == 2:
                rec2 = Prism(length, width, height, boxid)
                prisms.append(rec2)
            elif numOfRec == 3:
                rec3 = Prism(length, width, height, boxid)
                prisms.append(rec3)
            elif numOfRec == 4:
                rec4 = Prism(length, width, height, boxid)
                prisms.append(rec4)
            elif numOfRec == 5:
                rec5 = Prism(length, width, height, boxid)
                prisms.append(rec5)
            elif numOfRec == 6:
                rec6 = Prism(length, width, height, boxid)
                prisms.append(rec6)
            elif numOfRec == 7:
                rec7 = Prism(length, width, height, boxid)
                prisms.append(rec7)

            numOfRec += 1
            print(menu)
            choice = input("Choice: ")


        if choice == "2":
            found = False
            while found == False:
                try:
                    recToPrint = int(input("Which one(0-6): "))
                    print(prisms[recToPrint])
                    found = True
                except (IndexError, ValueError):
                    print("Rectangle not found")


            print(menu)
            choice = input("Choice: ")

        if choice == "3":
            for i in prisms:
                print(i)

        print(menu)
        choice = input("Choice: ")


main()

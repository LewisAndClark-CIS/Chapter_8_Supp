
class Create_Rectangle(object):

    def __init__(self, length, width, ID):
        self.length = length
        self.width = width
        self.ID = ID

    def __str__(self):
        strprint = "\nRectangle ID: " + str(self.ID) + "\n"
        strprint += "Length: "+ str(self.length) + "\n"
        strprint += "Width: " + str(self.width) + "\n"
        strprint += "Permimeter: " + str((self.width * 2) + (self.length * 2)) + "\n"
        strprint += "Area: " + str((self.width) * (self.length))
        strprint += "\n"
        return strprint


listofboxes = []
totalBoxes = 1
menu = """
        0 - Create Rectangle
        1 - Print a Rectangle
        2 - Print all Rectangles
        3 - Exit
        """
print(menu)
option = input("\nWhat would you like to do? (0-3): ")

while option != "3":
    if option == "0":
        length = int(input("Length: "))
        width = int(input("Width: "))
        ID = totalBoxes
        if totalBoxes == 1:
            rectangle = Create_Rectangle(length, width, ID)
            listofboxes.append(rectangle)
        elif totalBoxes == 2:
            rectangle_2 = Create_Rectangle(length, width, ID)
            listofboxes.append(rectangle_2)
        elif totalBoxes == 3:
            rectangle_3 = Create_Rectangle(length, width, ID)
            listofboxes.append(rectangle_3)
        totalBoxes += 1
    if option == "1":
        thisIsTrue = 1
        while thisIsTrue:
            try:
                if listofboxes:
                    print("There are " + str(len(listofboxes)) + " boxes already created.\n")
                    the_rect = int(input("Which one, (0-3) 0 being the first: "))
                    print(listofboxes[the_rect])
                    thisIsTrue = False
                else:
                    print("You have not created any rectangle yet.")
                    break
                
            except (IndexError, ValueError):
                print("That rectangle does not exist.")
    if option == "2":
        if listofboxes:
            for i in listofboxes:
                print(i)
        else:
            print("There are no rectangles to print")

    print(menu)
    option = input("\nWhat would you like to do?: ")


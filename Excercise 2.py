
class Create_Prism(object):

    def __init__(self, length, width, height, ID):
        self.length = length
        self.width = width
        self.ID = ID
        self.height = height

    def __str__(self):
        strprint = "\nPrism ID: " + str(self.ID) + " units\n"
        strprint += "Length: "+ str(self.length) + " units\n"
        strprint += "Width: " + str(self.width) + " units\n"
        strprint += "Surface Area: " + str(2 * ((self.width * self.length) + (self.height * self.length) + (self.height * self.width))) + " units\n"
        strprint += "Volume: " + str((self.height) * (self.width) * (self.length)) + " units"
        strprint += "\n"
        return strprint


listofboxes = []
totalBoxes = 1
menu = """
        0 - Create A Prism
        1 - Print a Prism
        2 - Print all Prisms
        3 - Exit
        """

print(menu)

option = input("\nWhat would you like to do? (0-3): ")

while option != "3":

    
    if option == "0":
        length = int(input("Length: "))
        width = int(input("Width: "))
        height = int(input("Height: "))
        ID = totalBoxes

        if totalBoxes == 1:
            prism = Create_Prism(length, width, height, ID)
            listofboxes.append(prism)
        elif totalBoxes == 2:
            prism_2 = Create_Prism(length, width, height, ID)
            listofboxes.append(prism_2)
        elif totalBoxes == 3:
            prism_3 = Create_Prism(length, width, height, ID)
            listofboxes.append(prism_3)
        totalBoxes += 1
    if option == "1":
        thisIsTrue = 1
        while thisIsTrue:
            try:
                if listofboxes:
                    print("There are " + str(len(listofboxes)) + " boxes already created.\n")
                else:
                    print("You have not created any prisms yet.")
                the_prism = int(input("Which one, (0-3) 0 being the first: "))
                print(listofboxes[the_prism])
                thisIsTrue = False
            except (IndexError, ValueError):
                print("That prism does not exist.")
    if option == "2":
        if listofboxes:
            for i in listofboxes:
                print(i)
        else:
            print("There are no boxes to print")

    print(menu)
    option = input("\nWhat would you like to do?: ")


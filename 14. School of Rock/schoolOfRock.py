print("-------------------------------------------")
print("Welcome to School Of Rock!")
print("-------------------------------------------")

bands = ["The Weeknd", "The Beatles", "One Direction", "The Chainsmokers", "Maroon 5"]


def checkBandInList(band):
    if band in bands:
        return True
    else:
        return False


def printAllBands():
    if len(bands) == 0:
        print("There are no bands on the list.")
    else:
        for i in range(0, len(bands)):
            print(i + 1, ". ", bands[i], sep="")

        print("There's a total of ", len(bands), " bands", sep="")


def findStartingLetterBand(firstLetter):
    found = False

    for band in bands:
        if firstLetter.lower() == band[0].lower():
            print(band)
            found = True

    if found == False:
        print("No bands start with that letter.")


def deleteBand(band):
    if band in bands:
        bands.remove(band)
        print(band, "deleted from the list.")
    else:
        print("This band is not on the list.")


while True:

    print("""
1 - Enter a new band
2 - Print out list of favorite bands
3 - Search if a band is already on the list
4 - Delete a band from the list
5 - Sort the list of bands alphabetically from A-Z
6 - Display bands starting with a letter
7 - Sort the list alphabetically from Z-A
8 - Exit
""")

    choice = int(input("User choice: "))

    if choice == 1:

        newBand = input("Enter the band you want to add: ")

        if checkBandInList(newBand):
            print("This band is already included.")
        else:
            bands.append(newBand)
            print(newBand, "added to the list!")

    elif choice == 2:

        printAllBands()

    elif choice == 3:

        searchBand = input("Enter the band you want to search: ")

        if checkBandInList(searchBand):
            print("Yes, this band is on the list")
        else:
            print("No, this band is not yet in the list")

    elif choice == 4:

        deleteBandName = input("Enter the band you want to delete: ")
        deleteBand(deleteBandName)

    elif choice == 5:

        bands.sort()
        print("The bands have been sorted alphabetically.")

    elif choice == 6:

        startingLetter = input("Enter a letter: ")
        findStartingLetterBand(startingLetter)

    elif choice == 7:

        bands.sort(reverse=True)
        print("The bands have been sorted from Z-A.")

    elif choice == 8:

        print("Thank you for using School Of Rock!")
        break

    else:

        print("Invalid choice. Please choose a number from 1-8.")


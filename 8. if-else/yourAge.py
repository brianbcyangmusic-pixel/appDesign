import random
print("------------------------------")
print("Welcome to the Movie Theater!")
print("------------------------------")


moviesTitle = [
    "28 Years Later [Horror 18+]",
    "The Conjuring: Last Rites [Horror 18+]", 
    "Fantastic Four [Action PG-13]", 
    "The Bad Guys II [Family G]", 
    "Superman [Action PG-13]", 
    "Jurassic World [Adventure PG-13]", 
    "Freakier Friday[Comedy PG-13]", 
    "Hamilton [Drama PG-13]", 
    "The Lion King [Family G]"
]

moviesDescription = [
    "A group of survivors of the rage virus live on a small island. When one of the group leaves the island on a mission into the mainland, he discovers secrets, wonders, and horrors that have mutated not only the infected but other survivors.",
    "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.",
    "Four young outsiders teleport to an alternate and dangerous universe, which alters their physical form in shocking ways. The four must learn to harness their new abilities and work together to save Earth from a former friend turned enemy.",
    "The Bad Guys are back in this sequel to the hit animated film. When the gang is framed for a crime they didn't commit, they must go on the run to clear their names and prove that they're not as bad as they seem.",
    "An alien orphan is sent from his dying planet to Earth, where he grows up to become his adoptive home's first and greatest superhero.",
    "A new theme park, built on the original site of Jurassic Park, creates a genetically modified hybrid dinosaur, which escapes containment and goes on a killing spree.",
    "A mother and daughter who have been at odds with each other magically swap bodies and must learn to understand each other's lives in order to switch back.",
    "The story of American founding father Alexander Hamilton, an immigrant from the West Indies who became George Washington's right-hand man during the Revolutionary War and later the first U.S. Secretary of the Treasury.",
    "A young lion prince flees his kingdom after the murder of his father."
]

moviesAgeLimite = [
    18,
    18,
    13,
    0,
    13,
    13,
    13,
    13,
    0
]

def startTitle():
    print("------------------------------")
    print("What do you want to watch?")
    print("------------------------------")

def displayMovies():
    for i, movie in enumerate(moviesTitle, start=1):
        print(f"{i}: {movie}")
    print(f"{len(moviesTitle) + 1}: Want a Suggestion?")
    print(f"{len(moviesTitle) + 2}: Exit")

def checkAge():
    global tempN
    tempN = []
    for i in range(len(moviesAgeLimite)):
        if moviesAgeLimite[i] <= age:
            tempN.append(i)

def printFeedback():
    if(age >= 18):
        print("Welcome to the massacre!")
    elif(age >= 14):
        print("Ah you thought you could sneak in here didn't you, young blood? Better go get your mommy or daddy!")
    elif(age >= 7):
        print("Nice try kiddie, the horror of this movie is not for the innocent-minded!")
    elif(age >= 1):
        print("You're joking right? Let me go get you some Teletubbies vids!")
    else:
        print("You are not even born yet, how did you even get here?")

age = int(input("Enter your age: "))

while True:
    startTitle()
    displayMovies()
    choice = int(input("Your choice: "))
    checkAge()
    if choice == len(moviesTitle) + 1:
        print("Here are some suggestions for you:")
        for i in tempN:
            print(f"{i + 1}: {moviesTitle[i]}")

    if choice == len(moviesTitle) + 2:
        break
    else:
        if choice - 1 in tempN:
            print("------------------------------")
            print(f"You have selected: {moviesTitle[choice - 1]}")
            print(f"Description: {moviesDescription[choice - 1]}")
            print("------------------------------")
            print("Would you like to purchase the ticket for this movie?")
            print(f"1: Yes for {random.randint(200, 1000)}$")
            print("2: No")
            purchase_choice = int(input("Your choice: "))
            if purchase_choice == 1:
                print("------------------------------")
                print("Thank you for your purchase! Enjoy the movie!")
                print("------------------------------")
            else:
                print("------------------------------")
                print("Okay, maybe next time!")
                print("------------------------------")
        else:
            print("------------------------------")
            printFeedback()
            print("------------------------------")

    print("------------------------------")
    print("Would you like to choose another movie?")
    print("1: Yes")
    print("2: No")
    another_choice = int(input("Your choice: "))
    if another_choice == 2:
        break


print("------------------------------")
print("Thank you for visiting the Movie Theater!")
print("------------------------------")







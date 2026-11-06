characters = ["Mickey Mouse", "Donald Duck", "Goofy", "Pluto", "Daisy Duck"]

description = ["Mickey Mouse is a cartoon character created by Walt Disney and Ub Iwerks in 1928. He is an anthropomorphic mouse who typically wears red shorts, large yellow shoes, and white gloves.",
               "Donald Duck is a cartoon character created by Walt Disney in 1934. He is an anthropomorphic white duck with a yellow-orange bill, legs, and feet. He typically wears a sailor suit with a bow tie and a hat.",
               "Goofy is a cartoon character created by Walt Disney in 1932. He is an anthropomorphic dog who typically wears a hat, vest, and pants. He is known for his clumsiness and distinctive laugh.",
               "Pluto is a cartoon character created by Walt Disney in 1930. He is an anthropomorphic dog who typically wears a collar and is known for his loyalty to Mickey Mouse.",
               "Daisy Duck is a cartoon character created by Walt Disney in 1940. She is an anthropomorphic white duck who typically wears a bow, blouse, and skirt. She is known for her sophisticated and sassy personality."]

movies = ["Mickey Mouse Clubhouse", "DuckTales", "Goof Troop", "Pluto's Christmas Tree", "Daisy Duck's Diary"]

print("Welcome to the Movie Database!")
print("You can add characters, remove them, and view their descriptions.")
print("-------------------------------------------------------")

while True:
    print("Please choose an option from the menu below:")
    print('''
            1) add a new character
            2) remove a character by typing their name
            3) print all characters
            4) print all characters backwards
            5) print every second character
            6) enter a character name and it prints their description
            7) print all characters names starting with _____
            8) print all characters in alphabetical order
            9) print all characters from _______show
        ''')

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        name = input("Enter the character's name: ")
        des = input("Enter a description for the character: ")
        mov = input("Enter a movie show for the character: ")
        characters.append(str(name))
        description.append(str(des))
        movies.append(str(mov))

    if choice == 2:
        name = input("Enter the character's name to remove: ")
        if name in characters:
            index = characters.index(name)
            characters.pop(index)
            description.pop(index)
            movies.pop(index)
            print(f"{name} has been removed from the database.")
        else:
            print(f"{name} not found in the database.")

    if choice == 3:
        print("-------------------------------------------------------")
        print("All characters in the database:")
        for name in characters:
            print(name)
        print("-------------------------------------------------------")

    if choice == 4:
        print("-------------------------------------------------------")
        print("All characters in the database (backwards):")
        for name in reversed(characters):
            print(name)
        print("-------------------------------------------------------")

    if choice == 5:
        print("Every second character in the database:")
        for i in range(1, len(characters), 2):
            print(characters[i])

    if choice == 6:
        name = input("Enter the character's name to view their description: ")
        if name in characters:
            index = characters.index(name)
            print(f"Description for {name}: {description[index]}")
        else:
            print(f"{name} not found in the database.")

    if choice == 7:
        letter = input("Enter the starting letter: ")
        print(f"Characters starting with '{letter}':")
        for name in characters:
            if name.startswith(letter):
                print(name)

    if choice == 8:
        sortedCharacter = sorted(characters)
        for i in sortedCharacter:
            print(i)

    if choice == 9:
        characterNum = []
        chosenMovie = input("Please input a movie show: ") 
        for i in movies:
            if chosenMovie == i:
                characterNum.append(movies.index(i))
        for i in characterNum:
            print(characters[i])

    input("\nPress ENTER when ready!")


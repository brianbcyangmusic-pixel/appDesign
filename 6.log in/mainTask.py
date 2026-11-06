userList = [
    "Brian",
    "Bob", 
    "Kyle",
    "Dylan",
    "Jarvis",
    "Justin",
]

passwordList = [
    12345678,
    87654321,
    11111111,
    12345678,
    87654321,
    11111111,
]

accessLevel = [
    "full",
    "semi",
    "basic",
    "basic",
    "full",
    "semi"
]

trials = 3
loggedIn = False


print("-----------------------------------------------------------------")
print("Welcome to the Military Capabilities Database")
print("-----------------------------------------------------------------")

while True:
    print("Please enter your username")
    name = input("Username: ")
    print("Please enter your password")
    password = input("Password: ")
    if name in userList and int(password) in passwordList:
        print("-----------------------------------------------------------------")
        print("Welcome agent", name, "you're now logged in!")
        userNumber = userList.index(name)
        loggedIn = True
        userLevel = accessLevel[userNumber]
        break
    else:
        trials -= 1
        print("Incorrect username or password.", trials, "trials left.")
        if trials == 0:
            print("You have used all your chance, Hacker.")
            break

while loggedIn == True:

    print("")

    if userLevel == "full":
        print("1: Air Capabilities")
        print("2: Naval Capabilities")
        print("3: Nuclear Capabilities")
        print("4: Special Units")
        print("5: Black Ops [CLASSIFIED]")

    elif userLevel == "semi":
        print("1: Air Capabilities")
        print("2: Naval Capabilities")
        print("3: Nuclear Capabilities")
        print("4: Special Units")

    else:
        print("1: Air Capabilities")
        print("2: Naval Capabilities")

    print("")
    userChoice = input("Choose an option: ")

    if userChoice == "1":
        print("Air Capabilities: Advanced aircraft and aerial technology.")

    elif userChoice == "2":
        print("Naval Capabilities: Ships, submarines, and naval technology.")

    elif userChoice == "3" and userLevel != "basic":
        print("Nuclear Capabilities: CLASSIFIED INFORMATION.")

    elif userChoice == "4" and userLevel == "full":
        print("Special Units: CLASSIFIED SPECIAL OPERATIONS INFORMATION.")

    elif userChoice == "5" and userLevel == "full":
        print("Black Ops: TOP SECRET INFORMATION.")

    else:
        print("You do not have access to this information.")

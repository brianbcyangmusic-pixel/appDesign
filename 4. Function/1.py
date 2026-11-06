def morningGreeting(name, late):
    print("Good morning, " + name + "!", end=" ")
    print("Today is going to be an amazing day!")
    if(late == True):
        print("You are late! come'on!")



morningGreeting("Dylan", False)
morningGreeting("Justin", True)
morningGreeting("Brian", False)

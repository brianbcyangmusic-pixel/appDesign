def bmi(weight, height):
    Bmi = height ** 2
    Bmi = weight / Bmi
    return Bmi


def printCharacter(name, weight, height, note):
    characterBMI = round(bmi(weight, height), 2)

    print(name)
    print("---------------")
    print("height:", height, "meters")
    print("weight:", weight, "kg")
    print("BMI:", characterBMI)
    print("Note:", note)
    print()


printCharacter("Luke Skywalker", 73, 1.72, "A true Jedi.")
printCharacter("Princess Leia", 51, 1.55, "A strong leader of the Rebellion.")
printCharacter("Yoda", 13, 0.66, "the shorter the better.")
printCharacter("Chewbacca", 112, 2.28, "good partner of my favorite charactor.")
printCharacter("Rey Skywalker", 54, 1.70, "who?")
printCharacter("Darth Sidious", 75, 1.78, "Unlimited power!")
printCharacter("Darth Vader", 120, 2.03, "soooo dark.")
printCharacter("Jabba the Hutt", 1358, 1.75, "very fat.")
printCharacter("Han Solo", 80, 1.8, "My FAVORITE chatactor!")


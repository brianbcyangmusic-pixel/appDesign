nameList = [
    "lukeskywalker",
    "princessleia",
    "yoda",
    "chewbacca",
    "reyskywalker",
    "darthsidious",
    "darthvader",
    "jabbathehutt",
    "hansolo",
]

weightList = [
    73,
    51,
    13,
    112,
    54,
    75,
    120,
    1358,
    80,
]

heightList = [
    1.72,
    1.55,
    0.66,
    2.28,
    1.70,
    1.78,
    2.03,
    1.75,
    1.8,
]

def bmi(weight, height):
    Bmi = height ** 2
    Bmi = weight / Bmi
    return Bmi


def weightClassification(BMI):
    if BMI >= 40:
        return "Very severely obese"
    elif BMI >= 35:
        return "Severely obese"
    elif BMI >= 30:
        return "Moderately obese"
    elif BMI >= 25:
        return "Overweight"
    elif BMI >= 18.5:
        return "Normal (healthy weight)"
    elif BMI >= 16:
        return "Underweight"
    elif BMI >= 15:
        return "Severely underweight"
    else:
        return "Very severely underweight"


def printWeightScale(BMI):

    # Colors
    GREEN = "\033[32m"
    RED = "\033[31m"
    ORANGE = "\033[33m"
    BLACK = "\033[30m"
    RESET = "\033[0m"

    # Decide the position on the 8-point scale
    if BMI < 15:
        scale = 1
        color = ORANGE

    elif BMI < 16:
        scale = 2
        color = ORANGE

    elif BMI < 18.5:
        scale = 3
        color = ORANGE

    elif BMI < 25:
        scale = 4
        color = GREEN

    elif BMI < 30:
        scale = 5
        color = RED

    elif BMI < 35:
        scale = 5
        color = RED

    elif BMI < 40:
        scale = 6
        color = RED

    else:
        scale = 8
        color = RED

    # Print the scale
    print("Weight Scale:")
    print(color + "#" * scale + BLACK + "#" * (8 - scale) + RESET)


def printCharacter(name):
    global characterBMI
    global characterHeight
    global characterWeight

    characterNumber = nameList.index(name)

    # Don't use -1 here!
    characterWeight = weightList[characterNumber]
    characterHeight = heightList[characterNumber]

    characterBMI = round(
        bmi(characterWeight, characterHeight),
        2
    )

    print(name)
    print("---------------")
    print("height:", characterHeight, "meters")
    print("weight:", characterWeight, "kg")
    print("BMI:", characterBMI)
    print("Weight Classification:", weightClassification(characterBMI))

    printWeightScale(characterBMI)

    print()



def healthPlan():
    print("Would you like to hear a recommended health plan?(yes/no)")
    answer = input()

    if "y" in answer.lower():
        backToNormalWeight()


def backToNormalWeight():
    print("---------------")
    if characterBMI < 18.5:
        print("You are underweight, you should eat more and gain some weight!")
        print(
            "You need to gain at least", round(18.5 * (characterHeight ** 2) - characterWeight, 2),
            "kg to reach a healthy weight!"
        )

    elif characterBMI > 25:
        print("You are overweight, you should exercise more and lose some weight!")
        print(
            "You need to lose at least", round(characterWeight - 25 * (characterHeight ** 2), 2),
            "kg to reach a healthy weight!"
        )
    print("---------------")


while True:

    print("Please enter a character name: ")
    characterName = input()

    characterName = characterName.lower()

    while " " in characterName:
        characterName = characterName.replace(" ", "")

    if characterName in nameList:

        printCharacter(characterName)

        healthPlan()

        print("Would you like to search for another character?(yes/no)")
        respond = input()

        if "y" in respond.lower():
            continue
        else:
            break

    else:
        print("not found!")
        continue
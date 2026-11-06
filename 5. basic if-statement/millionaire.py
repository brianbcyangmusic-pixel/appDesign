import random
money = 0

print("Ready to play Who Wants to Be a Millionaire?")

questions = [
    "Who is the current president of the USA?\nA- Benjamin Franklin\nB- IShowSpeed\nC- Barack Obama\nD- Donald Trump\n",

    "What is the largest planet in our solar system?\nA- Earth\nB- Mars\nC- Jupiter\nD- Venus\n",

    "What is the capital of France?\nA- London\nB- Paris\nC- Rome\nD- Madrid\n",

    "How many continents are there?\nA- 5\nB- 6\nC- 7\nD- 8\n",

    "What is H2O?\nA- Oxygen\nB- Hydrogen\nC- Water\nD- Salt\n",

    "Which animal is known as the King of the Jungle?\nA- Tiger\nB- Lion\nC- Elephant\nD- Bear\n",

    "Who wrote Romeo and Juliet?\nA- William Shakespeare\nB- J.K. Rowling\nC- Mark Twain\nD- Charles Dickens\n",

    "What is the fastest land animal?\nA- Lion\nB- Cheetah\nC- Horse\nD- Tiger\n",

    "Which country built the Great Wall?\nA- Japan\nB- India\nC- China\nD- Korea\n",

    "What is 12 x 12?\nA- 124\nB- 132\nC- 144\nD- 156\n",

    "Which planet is known as the Red Planet?\nA- Venus\nB- Mars\nC- Jupiter\nD- Mercury\n",

    "What is the capital of Japan?\nA- Seoul\nB- Beijing\nC- Tokyo\nD- Kyoto\n",

    "Who was the first person to walk on the Moon?\nA- Neil Armstrong\nB- Elon Musk\nC- Buzz Lightyear\nD- Albert Einstein\n",

    "Which ocean is the largest?\nA- Atlantic Ocean\nB- Indian Ocean\nC- Arctic Ocean\nD- Pacific Ocean\n",

    "What is the chemical symbol for gold?\nA- Go\nB- Gd\nC- Au\nD- Ag\n"
]

answers = [
    "d",
    "c",
    "b",
    "c",
    "c",
    "b",
    "a",
    "b",
    "c",
    "c",
    "b",
    "c",
    "a",
    "d",
    "c"
]

money_values = [
    100,
    200,
    300,
    500,
    1000,
    2000,
    4000,
    8000,
    16000,
    32000,
    64000,
    125000,
    250000,
    500000,
    1000000
]

for i in range(len(questions)):
    print("\nQuestion", i + 1, "- Worth $", money_values[i])

    answer = input(questions[i])

    if answer.lower() == answers[i]:
        money += money_values[i]
        print("Correct! You now have $", money)
    else:
        money = 0
        print("Too bad, so sad!")
        print("You have $0")
        break

print("\nGame over!")
print("You finished with $", money)
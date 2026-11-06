import os
import sys
import time

def play_intro():
    answer = None
    title = "LOADING GAME........."
    for i in range(len(title) + 1):
        print(f"\r{title[:i]}", end="")
        time.sleep(0.05)
    while answer == None:
        answer = input("\nPress ENTER to start!")

def transition_animation():
    print("-----------------------------------------------------")
    print("You are about to make a choice...")
    for i in range(3):
        print(".", end="")
        time.sleep(0.5)
    print("\n-----------------------------------------------------")

def textEngine(title, delay=0.03, new_line=True):
    for char in title:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(delay)
    if new_line:
        print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')


def get_choice(prompt, options):
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        print("Invalid choice. Please try again.")

def lose_life(lives):
    lives -= 1
    print("\nYou lost one life.")
    print(f"Lives remaining: {lives}")
    return lives

def checkpoint(lives):
    print("\n-----------------------------------------------------")
    print("CHECKPOINT REACHED")
    print("Your progress has been saved.")
    print(f"Lives remaining: {lives}")
    print("-----------------------------------------------------")
    return lives

def logic_puzzle(lives):
    textEngine("\nA stone tablet appears in front of you.")
    textEngine("The tablet asks:")
    textEngine("If two numbers add up to 10 and one number is 6, what is the other number?")
    print("1. 3")
    print("2. 4")
    print("3. 5")
    print("4. 6")

    answer = get_choice("Enter your answer: ", ["1", "2", "3", "4"])

    if answer == "2":
        textEngine("Correct. The stone door opens.")
        return lives, True
    else:
        lives = lose_life(lives)
        return lives, False

def pattern_puzzle(lives):
    textEngine("\nYou find another ancient puzzle.")
    textEngine("Complete the pattern:")
    textEngine("2, 4, 6, 8, ?")
    print("1. 9")
    print("2. 10")
    print("3. 11")
    print("4. 12")

    answer = get_choice("Enter your answer: ", ["1", "2", "3", "4"])

    if answer == "2":
        textEngine("Correct. A hidden passage opens.")
        return lives, True
    else:
        lives = lose_life(lives)
        return lives, False

def memory_puzzle(lives):
    textEngine("\nThe final puzzle asks you to remember the symbols.")
    textEngine("Earlier, the temple showed you these symbols:")
    textEngine("SUN - MOON - STAR")
    time.sleep(2)

    clear_screen()

    textEngine("Which symbol was shown in the middle?")
    print("1. SUN")
    print("2. MOON")
    print("3. STAR")
    print("4. CLOUD")

    answer = get_choice("Enter your answer: ", ["1", "2", "3", "4"])

    if answer == "2":
        textEngine("Correct. You have completed the Temple of Knowledge.")
        return lives, True
    else:
        lives = lose_life(lives)
        return lives, False

def temple_of_knowledge(lives):
    clear_screen()
    textEngine("TEMPLE OF KNOWLEDGE")
    textEngine("You enter an ancient temple filled with mysterious writing.")
    textEngine("The temple contains three challenges.")
    time.sleep(1)

    lives, correct = logic_puzzle(lives)

    if lives <= 0:
        return lives, False

    if correct:
        textEngine("You continue deeper into the temple.")
        time.sleep(1)

    lives, correct = pattern_puzzle(lives)

    if lives <= 0:
        return lives, False

    if correct:
        textEngine("The temple begins to glow.")
        time.sleep(1)

    lives, correct = memory_puzzle(lives)

    if lives <= 0:
        return lives, False

    if correct:
        textEngine("Since you learned all the knowledge stored in the temple,")
        textEngine("you are ready to enter the next stage.")
        return lives, True

def meet_npc(lives):
    clear_screen()
    textEngine("You meet a mysterious gatekeeper.")
    textEngine("The gatekeeper stands in front of a large stone entrance.")
    textEngine("He looks at you and says:")
    textEngine('"Who are you?"')

    print("\n1. I am looking for answers.")
    print("2. I am the prince of this kingdom.")
    print("3. Get out of my way bro.")

    choice = get_choice("What do you say? ", ["1", "2", "3"])

    if choice == "1":
        textEngine("\nThe gatekeeper looks interested.")
        textEngine('"Then perhaps you are worthy to continue."')
        return lives, True

    elif choice == "2":
        textEngine("\nThe gatekeeper does not believe you.")
        textEngine('"Prove that you are truly the prince."')
        return lives, True

    elif choice == "3":
        textEngine("\nThe gatekeeper becomes angry.")
        textEngine("GET OUT OF MY WAY BRO.")
        lives = lose_life(lives)

        if lives <= 0:
            return lives, False

        textEngine("The gatekeeper allows you to leave.")
        return lives, True

def village_path(lives):
    clear_screen()
    textEngine("You enter an abandoned village.")
    textEngine("The village is empty, but you notice an old building.")
    textEngine("It appears to be a restaurant.")

    print("\n1. Enter the restaurant")
    print("2. Continue through the village")

    choice = get_choice("Enter 1 or 2: ", ["1", "2"])

    if choice == "1":
        textEngine("\nYou enter the restaurant.")
        textEngine("Inside, you discover an old map of the destroyed kingdom.")
        textEngine("The map reveals a hidden route to the second dungeon.")
        return lives, True

    elif choice == "2":
        textEngine("\nYou continue through the village.")
        textEngine("The road leads you toward a mysterious door.")
        return lives, True

def valley_path(lives):
    clear_screen()
    textEngine("You enter a dark valley.")
    textEngine("Three escapees are hiding near the mountain.")
    textEngine("They warn you about dangerous creatures ahead.")

    print("\n1. Hide and wait for the danger to pass")
    print("2. Try to stop the danger")

    choice = get_choice("Enter 1 or 2: ", ["1", "2"])

    if choice == "1":
        textEngine("\nYou hide behind a large rock.")
        textEngine("The danger passes without noticing you.")
        textEngine("You find a safe route through the valley.")
        return lives, True

    elif choice == "2":
        textEngine("\nYou try to stop the danger.")
        textEngine("Unfortunately, the creature notices you.")
        lives = lose_life(lives)

        if lives <= 0:
            return lives, False

        textEngine("You escape into a nearby passage.")
        return lives, True

def choose_route(lives):
    clear_screen()
    textEngine("You arrive at a fork in the road.")
    textEngine("Two possible routes are in front of you.")

    print("\n1. Valley")
    print("2. Restaurant")

    choice = get_choice("Choose a route: ", ["1", "2"])

    if choice == "1":
        return valley_path(lives)

    elif choice == "2":
        return village_path(lives)

def second_dungeon(lives):
    clear_screen()
    textEngine("You arrive at the second dungeon.")
    textEngine("A strange gatekeeper blocks the entrance.")
    textEngine('"I am the gate keeper of the second dungeon."')
    textEngine('"You must answer my questions to pass."')

    print("\n1. Ask if you can enter")
    print("2. Walk away")

    choice = get_choice("Enter 1 or 2: ", ["1", "2"])

    if choice == "2":
        textEngine("\nYou turn around and leave the dungeon.")
        textEngine("Unfortunately, you step on a hidden poisonous creature.")
        textEngine("You have died. Game Over.")
        return lives, False

    elif choice == "1":
        textEngine("\nThe gatekeeper allows you to enter.")
        return dungeon_challenges(lives)

def dungeon_challenges(lives):
    textEngine("\nA goblin is guarding a bridge.")
    textEngine("You must answer three questions correctly.")
    textEngine("You only get two chances.")

    chances = 2
    correct_answers = 0

    while chances > 0 and correct_answers < 3:
        textEngine("\nQuestion 1: What is 5 + 5?")
        print("1. 8")
        print("2. 10")
        print("3. 12")

        answer = get_choice("Enter your answer: ", ["1", "2", "3"])

        if answer == "2":
            textEngine("Correct.")
            correct_answers += 1
        else:
            chances -= 1
            print(f"Wrong. Chances remaining: {chances}")

        if chances <= 0:
            break

        if correct_answers < 3:
            textEngine("\nQuestion 2: Which number comes next?")
            textEngine("3, 6, 9, ?")
            print("1. 10")
            print("2. 11")
            print("3. 12")

            answer = get_choice("Enter your answer: ", ["1", "2", "3"])

            if answer == "3":
                textEngine("Correct.")
                correct_answers += 1
            else:
                chances -= 1
                print(f"Wrong. Chances remaining: {chances}")

        if chances <= 0:
            break

        if correct_answers < 3:
            textEngine("\nQuestion 3: What was the middle symbol in the temple?")
            print("1. SUN")
            print("2. MOON")
            print("3. STAR")

            answer = get_choice("Enter your answer: ", ["1", "2", "3"])

            if answer == "2":
                textEngine("Correct.")
                correct_answers += 1
            else:
                chances -= 1
                print(f"Wrong. Chances remaining: {chances}")

    if correct_answers >= 3:
        textEngine("\nYou answered all three questions correctly.")
        textEngine("The goblin moves away from the bridge.")
        return lives, True
    else:
        textEngine("\nYou failed to answer the questions.")
        textEngine("The goblin refuses to let you pass.")
        textEngine("Game Over.")
        return lives, False

def final_stage(lives):
    clear_screen()
    textEngine("You have completed the dangerous journey.")
    textEngine("The knowledge from the temple helped you survive.")
    textEngine("The gatekeepers and puzzles tested your decisions.")
    textEngine("You finally discover the truth about the destroyed kingdom.")
    textEngine("The kingdom was destroyed because its people stopped learning.")
    textEngine("You now have the knowledge needed to rebuild it.")

    print("\n-----------------------------------------------------")
    print("CONGRATULATIONS!")
    print("YOU COMPLETED THE ADVENTURE!")
    print("-----------------------------------------------------")



# Main Game Loop start here
play_intro()
clear_screen()

print("-----------------------------------------------------")
print("Welcome to the Pick-A-Path Game!")
print("-----------------------------------------------------")
print("You will be presented with a series of choices.")
print("Your decisions will affect the outcome of your journey.")
print("Make your choices wisely.")
print("-----------------------------------------------------")

time.sleep(1)

player_name = input("\nEnter Player Name: ")

lives = 3

clear_screen()

textEngine(f"Welcome, {player_name}.")
textEngine("You wake up in a mysterious temple with no memory of how you got there.")
textEngine("You look around and find ancient writing on the walls.")
textEngine("The writing tells the story of a destroyed kingdom.")
textEngine("You must discover what happened and find a way to restore the kingdom.")

time.sleep(5)

textEngine("\nYou discover an ancient temple filled with knowledge.")
lives = checkpoint(lives)
next = None
if next == None:
    next = input("\nPress ENTER to continue!")

lives, completed = temple_of_knowledge(lives)

if not completed or lives <= 0:
    textEngine("\nYou were unable to complete the Temple of Knowledge.")
    textEngine("Game Over.")

lives, completed = meet_npc(lives)

if not completed or lives <= 0:
    textEngine("\nYour journey has ended.")
    textEngine("Game Over.")


lives, completed = choose_route(lives)

if not completed or lives <= 0:
    textEngine("\nYou could not continue your journey.")
    textEngine("Game Over.")


textEngine("\nYou continue deeper into the destroyed kingdom.")
time.sleep(1)

lives, completed = second_dungeon(lives)

if not completed or lives <= 0:
    textEngine("\nYou have reached the end of your journey.")
    textEngine("Game Over.")


final_stage(lives)

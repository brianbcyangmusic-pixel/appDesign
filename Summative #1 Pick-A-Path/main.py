import os
import sys
import time


# Colors
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"


def type_text(message, delay=0.03, color=CYAN):
    for character in message:
        print(f"{color}{character}{RESET}", end="")
        sys.stdout.flush()
        time.sleep(delay)
    print()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def continue_game():
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")


def ask_choice(prompt, choices):
    while True:
        choice = input(f"{YELLOW}{prompt}{RESET}").strip()

        if choice in choices:
            return choice

        print(f"{RED}Invalid choice. Please try again.{RESET}")


def lose_life(lives):
    lives -= 1
    print(f"\n{RED}You lost one life.{RESET}")
    print(f"{YELLOW}Lives remaining: {lives}{RESET}")
    return lives


def main():

    # Loading screen
    loading_message = "LOADING GAME........."

    for character_count in range(len(loading_message) + 1):
        print(
            f"\r{MAGENTA}{loading_message[:character_count]}{RESET}",
            end=""
        )
        time.sleep(0.05)

    continue_game()

    clear_screen()

    print(f"{MAGENTA}WELCOME TO THE PICK-A-PATH GAME!{RESET}")
    print(f"{WHITE}You will be presented with a series of choices.")
    print("Your decisions will affect the outcome of your journey.")
    print(f"{YELLOW}Make your choices wisely.{RESET}")

    time.sleep(1)

    player_name = input(
        f"\n{YELLOW}Enter Player Name: {RESET}"
    )

    lives = 3

    # The story begins
    clear_screen()

    type_text(f"Welcome, {player_name}.")
    type_text(
        "You wake up in a mysterious temple with no memory of how you got there."
    )
    type_text(
        "You look around and find ancient writing on the walls."
    )
    type_text(
        "The writing tells the story of a destroyed kingdom."
    )
    type_text(
        "You must discover what happened and find a way to restore the kingdom."
    )

    time.sleep(1)

    type_text(
        "\nYou discover an ancient temple filled with knowledge."
    )

    print(f"\n{MAGENTA}CHECKPOINT REACHED{RESET}")
    print(f"{GREEN}Your progress has been saved.{RESET}")
    print(f"{YELLOW}Lives remaining: {lives}{RESET}")

    continue_game()
    clear_screen()

    # Temple of Knowledge
    type_text(
        "TEMPLE OF KNOWLEDGE",
        color=MAGENTA
    )

    type_text(
        "You enter an ancient temple filled with mysterious writing."
    )
    type_text(
        "The temple contains three challenges."
    )

    time.sleep(1)

    # Puzzle 1
    type_text("\nA stone tablet appears in front of you.")
    type_text("The tablet asks:")
    type_text(
        "If two numbers add up to 10 and one number is 6, "
        "what is the other number?"
    )

    print(f"{YELLOW}1. 3")
    print("2. 4")
    print("3. 5")
    print(f"4. 6{RESET}")

    if ask_choice(
        "Enter your answer: ",
        ["1", "2", "3", "4"]
    ) == "2":

        type_text(
            "Correct. The stone door opens.",
            color=GREEN
        )

    else:
        lives = lose_life(lives)

    if lives <= 0:
        type_text(
            "\nYou were unable to complete the Temple of Knowledge.",
            color=RED
        )
        type_text("GAME OVER.", color=RED)
        return

    continue_game()
    clear_screen()

    # Puzzle 2
    type_text(
        "TEMPLE OF KNOWLEDGE",
        color=MAGENTA
    )

    type_text("You continue deeper into the temple.")
    type_text("You find another ancient puzzle.")
    type_text("Complete the pattern:")
    type_text("2, 4, 6, 8, ?")

    print(f"{YELLOW}1. 9")
    print("2. 10")
    print("3. 11")
    print(f"4. 12{RESET}")

    if ask_choice(
        "Enter your answer: ",
        ["1", "2", "3", "4"]
    ) == "2":

        type_text(
            "Correct. A hidden passage opens.",
            color=GREEN
        )

    else:
        lives = lose_life(lives)

    if lives <= 0:
        type_text(
            "\nYou were unable to complete the Temple of Knowledge.",
            color=RED
        )
        type_text("GAME OVER.", color=RED)
        return

    continue_game()

    # MEMORY PUZZLE

    clear_screen()

    type_text(
        "MEMORY CHALLENGE",
        color=MAGENTA
    )

    type_text(
        "The final puzzle asks you to remember the symbols."
    )

    type_text(
        "Remember these symbols carefully:"
    )

    type_text(
        "SUN - MOON - STAR",
        color=YELLOW
    )

    time.sleep(2)

    # NO ENTER HERE.
    # The screen clears automatically so the player
    # must remember the symbols.

    clear_screen()

    type_text(
        "Which symbol was shown in the middle?"
    )

    print(f"{YELLOW}1. SUN")
    print("2. MOON")
    print("3. STAR")
    print(f"4. CLOUD{RESET}")

    if ask_choice(
        "Enter your answer: ",
        ["1", "2", "3", "4"]
    ) == "2":

        type_text(
            "Correct. You have completed the Temple of Knowledge.",
            color=GREEN
        )

    else:
        lives = lose_life(lives)

    if lives <= 0:
        type_text(
            "\nYou were unable to complete the Temple of Knowledge.",
            color=RED
        )
        type_text("GAME OVER.", color=RED)
        return

    type_text(
        "\nSince you learned all the knowledge stored in the temple,"
    )
    type_text(
        "you are ready to enter the next stage."
    )

    continue_game()
    clear_screen()

    # GATEKEEPER

    type_text(
        "THE GATEKEEPER",
        color=MAGENTA
    )

    type_text(
        "You meet a mysterious gatekeeper."
    )
    type_text(
        "The gatekeeper stands in front of a large stone entrance."
    )
    type_text(
        "He looks at you and says:"
    )
    type_text(
        '"Who are you?"',
        color=YELLOW
    )

    print(f"\n{YELLOW}1. I am looking for answers.")
    print("2. I am the prince of this kingdom.")
    print(f"3. Get out of my way bro.{RESET}")

    choice = ask_choice(
        "What do you say? ",
        ["1", "2", "3"]
    )

    if choice == "1":

        type_text(
            "\nThe gatekeeper looks interested."
        )
        type_text(
            '"Then perhaps you are worthy to continue."',
            color=GREEN
        )

    elif choice == "2":

        type_text(
            "\nThe gatekeeper does not believe you."
        )
        type_text(
            '"Prove that you are truly the prince."',
            color=YELLOW
        )
        type_text(
            "He lets you continue, but warns you to be careful."
        )

    else:

        type_text(
            "\nThe gatekeeper becomes angry.",
            color=RED
        )
        type_text(
            "GET OUT OF MY WAY BRO.",
            color=RED
        )

        lives = lose_life(lives)

        if lives <= 0:
            type_text(
                "\nYour journey has ended.",
                color=RED
            )
            type_text(
                "GAME OVER.",
                color=RED
            )
            return

        type_text(
            "The gatekeeper allows you to continue."
        )

    continue_game()
    clear_screen()

    # CHOOSE A ROUTE

    type_text(
        "THE FORK IN THE ROAD",
        color=MAGENTA
    )

    type_text(
        "You arrive at a fork in the road."
    )
    type_text(
        "Two possible routes are in front of you."
    )

    print(f"\n{YELLOW}1. Valley")
    print(f"2. Abandoned Village{RESET}")

    route = ask_choice(
        "Choose a route: ",
        ["1", "2"]
    )

    if route == "1":

        # Valley path
        continue_game()
        clear_screen()

        type_text(
            "THE DARK VALLEY",
            color=MAGENTA
        )

        type_text(
            "You enter a dark valley."
        )
        type_text(
            "Three travelers are hiding near the mountain."
        )
        type_text(
            "They warn you about dangerous creatures ahead."
        )

        print(f"\n{YELLOW}1. Hide and wait for the danger to pass")
        print(f"2. Try to stop the danger{RESET}")

        valley_choice = ask_choice(
            "Enter 1 or 2: ",
            ["1", "2"]
        )

        if valley_choice == "1":

            type_text(
                "\nYou hide behind a large rock."
            )
            type_text(
                "The danger passes without noticing you."
            )
            type_text(
                "You find a safe route through the valley.",
                color=GREEN
            )

        else:

            type_text(
                "\nYou try to stop the danger.",
                color=YELLOW
            )
            type_text(
                "Unfortunately, the creature notices you.",
                color=RED
            )

            lives = lose_life(lives)

            if lives <= 0:
                type_text(
                    "\nYou could not continue your journey.",
                    color=RED
                )
                type_text(
                    "GAME OVER.",
                    color=RED
                )
                return

            type_text(
                "You escape into a nearby passage."
            )

    else:

        # Village path
        continue_game()
        clear_screen()

        type_text(
            "THE ABANDONED VILLAGE",
            color=MAGENTA
        )

        type_text(
            "You enter an abandoned village."
        )
        type_text(
            "The village is empty, but you notice an old building."
        )
        type_text(
            "It appears to be a restaurant."
        )

        print(f"\n{YELLOW}1. Enter the restaurant")
        print(f"2. Continue through the village{RESET}")

        village_choice = ask_choice(
            "Enter 1 or 2: ",
            ["1", "2"]
        )

        if village_choice == "1":

            type_text(
                "\nYou enter the restaurant."
            )
            type_text(
                "Inside, you discover an old map of the destroyed kingdom."
            )
            type_text(
                "The map reveals a hidden route to the second dungeon.",
                color=GREEN
            )

        else:

            type_text(
                "\nYou continue through the village."
            )
            type_text(
                "The road leads you toward a mysterious door."
            )

    continue_game()
    clear_screen()

    # SECOND DUNGEON

    type_text(
        "THE SECOND DUNGEON",
        color=MAGENTA
    )

    type_text(
        "You arrive at the second dungeon."
    )
    type_text(
        "A strange gatekeeper blocks the entrance."
    )
    type_text(
        '"I am the gatekeeper of the second dungeon."',
        color=YELLOW
    )
    type_text(
        '"You must answer my questions to pass."',
        color=YELLOW
    )

    print(f"\n{YELLOW}1. Ask if you can enter")
    print(f"2. Walk away{RESET}")

    dungeon_choice = ask_choice(
        "Enter 1 or 2: ",
        ["1", "2"]
    )

    if dungeon_choice == "2":

        type_text(
            "\nYou turn around and leave the dungeon."
        )
        type_text(
            "You walk away from the kingdom."
        )
        type_text(
            "You will never discover the truth.",
            color=RED
        )
        type_text(
            "GAME OVER.",
            color=RED
        )
        return

    type_text(
        "\nThe gatekeeper allows you to enter.",
        color=GREEN
    )

    continue_game()
    clear_screen()

    # GOBLIN CHALLENGE

    type_text(
        "THE GOBLIN'S BRIDGE",
        color=MAGENTA
    )

    type_text(
        "A goblin is guarding a bridge."
    )
    type_text(
        "You must answer three questions correctly."
    )
    type_text(
        "You only get two chances.",
        color=YELLOW
    )

    questions = [
        (
            "Question 1: What is 5 + 5?",
            ["1. 8", "2. 10", "3. 12"],
            "2"
        ),
        (
            "Question 2: Which number comes next?\n3, 6, 9, ?",
            ["1. 10", "2. 11", "3. 12"],
            "3"
        ),
        (
            "Question 3: What was the middle symbol in the temple?",
            ["1. SUN", "2. MOON", "3. STAR"],
            "2"
        )
    ]

    chances = 2
    correct_answers = 0

    while chances > 0 and correct_answers < len(questions):

        question, choices, correct_answer = questions[correct_answers]

        type_text(
            f"\n{question}",
            color=YELLOW
        )

        for choice in choices:
            print(f"{YELLOW}{choice}{RESET}")

        answer = ask_choice(
            "Enter your answer: ",
            ["1", "2", "3"]
        )

        if answer == correct_answer:

            type_text(
                "Correct.",
                color=GREEN
            )

            correct_answers += 1

        else:

            chances -= 1

            type_text(
                f"Wrong. Chances remaining: {chances}",
                color=RED
            )

    if correct_answers < len(questions):

        type_text(
            "\nYou failed to answer the questions.",
            color=RED
        )
        type_text(
            "The goblin refuses to let you pass.",
            color=RED
        )
        type_text(
            "GAME OVER.",
            color=RED
        )
        return

    type_text(
        "\nYou answered all three questions correctly.",
        color=GREEN
    )
    type_text(
        "The goblin moves away from the bridge.",
        color=GREEN
    )

    continue_game()
    clear_screen()

    # ENDING

    type_text(
        "THE TRUTH",
        color=MAGENTA
    )

    type_text(
        "You have completed the dangerous journey."
    )
    type_text(
        "The knowledge from the temple helped you survive."
    )
    type_text(
        "The gatekeepers and puzzles tested your decisions."
    )
    type_text(
        "You finally discover the truth about the destroyed kingdom."
    )

    type_text(
        "\nThe kingdom was destroyed because its people stopped learning.",
        color=YELLOW
    )

    type_text(
        "You now have the knowledge needed to rebuild it."
    )

    print()
    print(f"{GREEN}CONGRATULATIONS!")
    print(f"YOU COMPLETED THE ADVENTURE!{RESET}")


# Replay system
try:

    while True:

        main()

        replay_choice = ask_choice(
            "\nDo you want to play again? (y/n): ",
            ["y", "n"]
        )

        if replay_choice == "n":

            print(
                f"\n{CYAN}Thank you for playing! Goodbye.{RESET}"
            )

            break

except KeyboardInterrupt:

    print(
        f"\n\n{CYAN}Game stopped. Goodbye!{RESET}"
    )
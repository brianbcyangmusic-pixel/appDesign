import random

mainDeck = []
currentCard = None

dealer = []
player1 = []
player2 = []
player3 = []

numberToWord = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Jack",
    12: "Queen",
    13: "King"
}

# Create the deck
for i in range(1, 53):
    mainDeck.append(i)


def drawCard():
    return mainDeck.pop(0)


def getCardIdentity(unknownCard):
    if unknownCard <= 13:
        currentCardFamily = "hearts"
    elif unknownCard <= 26:
        currentCardFamily = "diamonds"
    elif unknownCard <= 39:
        currentCardFamily = "spades"
    else:
        currentCardFamily = "clubs"

    num = (unknownCard - 1) % 13 + 1
    currentCardNum = numberToWord[num]

    return currentCardFamily, currentCardNum


def printCard(which):
    family, num = getCardIdentity(which)
    print(num, "of", family)


def printHand(who):
    for card in who:
        printCard(card)


def dealCards(who, amount):
    for i in range(amount):
        who.append(drawCard())


# Main code begins
random.shuffle(mainDeck)

# Deal two cards to each player
dealCards(dealer, 2)
dealCards(player1, 2)
dealCards(player2, 2)
dealCards(player3, 2)

# Print each hand
print("Dealer's hand:")
printHand(dealer)

print("\nPlayer 1's hand:")
printHand(player1)

print("\nPlayer 2's hand:")
printHand(player2)

print("\nPlayer 3's hand:")
printHand(player3)

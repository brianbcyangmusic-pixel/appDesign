import random
name = input("what's your name: ")
print("Hello, " + name + "!")

mood = input("How are you feeling today? ")
if mood == "happy":
    print("That's great to hear!")
elif mood == "sad":
    print("I'm sorry to hear that. I hope your day gets better!")
elif mood == "angry":
    print("chill!!!")

while True:
    question = input("what's your question?")
    print("run out of token")

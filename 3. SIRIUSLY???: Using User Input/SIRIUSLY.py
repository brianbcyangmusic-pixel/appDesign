import random

print("SIRIUSLY: Hi my name is SIRIUSLY. I'm a super hyper intelligent AI and UNFORTUNATELY I'm here to answer any pathetically primitive questions you feel like asking me! So go ahead, ask away!")


print("SIRIUSLY: Hello User!")

# print("SIRIUSLY: Okay, " + name + ", you may ask me 5 questions.")

for i in range(5):
    print("SIRIUSLY: What's your question?")
    question = input("User: ")

    answers = [
        "You seriously don't know that? Please think harder.",
        "That is a really good question. You should think harder.",
        "Hmm... maybe try figuring it out yourself.",
        "Wow. That's what you're asking me?",
        "I could answer that, but I'm not going to.",
        "Seriously? You need an AI for THAT?",
        "I'm afraid that question is below my knowledge line."
    ]
    answer = random.choice(answers)
    print("SIRIUSLY:", answer)
    answers.remove(answer)

print("SIRIUSLY: THAT'S IT! You've used al your tokens.")
print("SIRIUSLY: Run out of tokens, please buy Premium to ask more questions.")
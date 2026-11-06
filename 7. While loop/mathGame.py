import random
point = 0
number1 = 0
number2 = 0
operatorChooser = 0
trueAnswer = 0
trueAnswered = None

operator = ["+", "-", "⨉", "÷"]

def trueAnswerCalculator(a, b, opera):
    global trueAnswer
    if opera == 0:
        trueAnswer = a + b
    elif opera == 1:
        trueAnswer = a - b
    elif opera == 2:
        trueAnswer = a * b
    elif opera == 3:
        trueAnswer = a / b
    return(trueAnswer)



print("---------------------------------------------")
print("Wellcome to Math challenge.")
print("---------------------------------------------")
while True:

    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operatorChooser = random.randint(0, 3)
    trueAnswered = trueAnswerCalculator(number1, number2, operatorChooser)

    while type(trueAnswered) == float and type(trueAnswered) != None:
        number1 = random.randint(1, 10)
        number2 = random.randint(1, 10)
        operatorChooser = random.randint(0, 3)
        trueAnswered = trueAnswerCalculator(number1, number2, operatorChooser)

    print("Question", str(point + 1), ",What is", number1, operator[operatorChooser], number2, "?")
    answer = input("Answer: ")

    if answer == str(trueAnswered):
        point += 1
        print("your right, currently you have ", point, "point(s)")
    else:
        print("Your Wrong, the correct answer is ", trueAnswered)

    if point == 20:
        break
print("Great, You've nailted the math game!!!")
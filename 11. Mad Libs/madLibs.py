red = "\033[1;31m"

end = "\033[0m"

questionList = [
    "1- verb(past tense)",
    "2- superlative (ex: prettiest or most beautiful)",
    "3- famous person",
    "4- profession (job)",
    "5- adjective",
    "6- verb ending in -ing",
    "7- number",
    "8- verb",
    "9- verb",
    "10- plural noun",
    "11- verb",
    "12- adjective ending in -er",
    "13- finish this comparison:   so fast that _____________",
    "14- terrible sports team",
    "15- position (sports) (ex: Point guard or Center)",
    "16- number <5",
    "17- position (sports) ",
    "18- number < 2",
    "19- a really huge number",
    "20- plural noun",
    "21- noun",
    "22- emotion",
    "23- adjective"
]

responses = []

print("Welcome to the Mad Libs game!")
print("Please enter the following words:")
for question in questionList:
    answer = input("question: " + question + ": ")
    responses.append(answer)

print("Thank you for playing!")
print("Here are your responses:")

print('''
    Last Friday, our class {red}{responses[0]}{end} onto the bus for what was supposed to be {red}{responses[1]}{end} field trip ever. Everyone was excited because we were going to meet {red}{responses[2]}{end}, who works as a {red}{responses[3]}{end}.

    When we arrived, however, the place looked extremely {red}{responses[4]}{end}. Instead of {red}{responses[5]}{end}, we were told that we had to wait {red}{responses[6]}{end} minutes before we could {red}{responses[7]}{end}. Our teacher tried to {red}{responses[8]}{end} the situation, but several {red}{responses[9]}{end} had already escaped from the building.

    We decided to {red}{responses[10]}{end} after them, but the {red}{responses[11]}{end} we moved, the harder it became to keep up. We were {red}{responses[12]}{end}, and suddenly we found ourselves inside {red}{responses[13]}{end}.

    Our teacher called for a {red}{responses[14]}{end}, but it took {red}{responses[15]}{end} hours to arrive. By then, we had somehow ended up at {red}{responses[16]}{end}. We only had {red}{responses[17]}{end} minute to figure out what to do before the school called us.

    The teacher said she had received {red}{responses[18]}{end} complaints from parents about the field trip. Meanwhile, the {red}{responses[19]}{end} were still running around, and someone had accidentally dropped a {red}{responses[20]}{end} into the teacher's bag.

    Everyone felt {red}{responses[21]}{end}, but somehow we made it back to school safely. Our principal described the entire experience as {red}{responses[22]}{end} and promised that our next field trip would be much more carefully planned.
    '''.format(red=red, responses=responses, end=end))
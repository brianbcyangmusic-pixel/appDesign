teacherMessage = ["Amazing! Nice job!", "Awesome! Almost Perfect!", "Almost there! Great effort!", "Pretty Good! Keep it up!"]
print(teacherMessage)
grade = int(input("Enter your grade: "))

if(grade >= 29):
    print("A+")
    print(teacherMessage[0])
elif(grade >= 26):
    print("A")
    print(teacherMessage[1])
elif(grade >= 24):
    print("A-")
    print(teacherMessage[2])
elif(grade >= 21):
    print("B+")
    print(teacherMessage[3])
elif(grade >= 19):
    print("B")
    print(teacherMessage[3])
elif(grade >= 17):
    print("B-")
    print(teacherMessage[3])    
elif(grade >= 15):
    print("C+")
elif(grade >= 13):
    print("C")
elif(grade >= 11):
    print("C-")
elif(grade >= 9):
    print("D")
else:
    print("F")
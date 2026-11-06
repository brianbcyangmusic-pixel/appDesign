count = 0
students = ["justin", "dylan", "brian", "bob", "eagan"]
students.append("bob")
if "bob" in students:
    for i in students:
        if i == "bob":
            count += 1
print("there's ", i, "bobs in this list.")

def checkStudent(who):
    if who in students:
        students.remove(who)
    else:
        print("no")
aaa = input("who??? ")
checkStudent(aaa)

for i in range(len(students) - 1, -1, -1):
    print(students[i])
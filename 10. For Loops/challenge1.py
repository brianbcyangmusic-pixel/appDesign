def countDown(n):
    for i in range(n, 0, -1):
        print(i)
    print("Blast off!")

def countUp(n):
    for i in range(1, n + 1):
        print(i)

countDown(5)
countUp(5)
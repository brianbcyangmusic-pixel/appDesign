def countdownOdd(n):
    if n % 2 == 0:
        n -= 1
    for i in range(n, 0, -2):
        print(i)
    print("Blast off!")

def countupOdd(n):
    if n % 2 == 0:
        n -= 1
    for i in range(1, n + 1, 2):
        print(i)

def countdownEven(n):
    if n % 2 != 0:
        n -= 1
    for i in range(n, 0, -2):
        print(i)
    print("Blast off!")

def countUpEven(n):
    if n % 2 != 0:
        n -= 1
    for i in range(2, n + 1, 2):
        print(i)



countdownOdd(10)
print("--------------------------")
countupOdd(10)
print("--------------------------")
countdownEven(10)
print("--------------------------")
countUpEven(10)
print("--------------------------")

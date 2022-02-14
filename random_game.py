from random import randrange
(randrange(10))

randomInput = (randrange(10))

print("Choose a number between 0 and 10")
userNumber = input()
userNumber = int(userNumber)

while True:
    if userNumber < randomInput:
        print("more")
        print("Choose a number between 0 and 10")
        userNumber = input()
        userNumber = int(userNumber)

    elif userNumber > randomInput:
        print("less")
        print("Choose a number between 0 and 10")
        userNumber = input()
        userNumber = int(userNumber)

    else:
        print("correct!")
        break

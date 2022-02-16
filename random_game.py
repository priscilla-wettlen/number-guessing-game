from random import randrange

def checkGuess(userInput, randomNum):
    if userInput == randomNum:
        return 'Correct!'
    if userInput > randomNum:
        return 'Less!'
    if userInput < randomNum:
        return 'More!'

def main():
    result = checkGuess(2, 4)
    print(result)

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

if __name__ == '__main__': #name (built-in) represents the name of the file we're in; #main is the script that we are running
    main()